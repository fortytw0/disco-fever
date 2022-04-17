from concurrent.futures import process
import json
import os
import time

'''
 Module imports
'''

from transformers import BertTokenizer, TFBertModel
import numpy as np

'''
Read Data
'''

with open('data/processed_samples.json') as f :
    processed_samples = json.load(f)


with open('configs/bert_repr_counter.txt') as f : 
    counter = int(f.read())


with open('data/repr_info.csv') as f : 
    repr_info = f.read()

'''
Program Variables
'''

data_dest_dir = 'data/repr/'

batch_size = 64

log_frequency = 500

num_samples = len(processed_samples)


'''
Environment Setup
'''

if not os.path.exists(data_dest_dir) : 
    os.mkdir(data_dest_dir)

'''
BERT Setup
'''

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bert = TFBertModel.from_pretrained('bert-base-uncased')

'''
Main
'''

batch_of_single_sentence_answers = []
batch_of_contextual_answers = []
batch_of_labels = []
batch_of_ids = []

batch_start_time = time.time()
program_start_time = time.time()

while counter < num_samples : 

    sample = processed_samples[counter]

    id = sample['id']
    print(id)
    claim = sample['claim']
    label = 1.0 if sample['label'] == 'SUPPORTS' else 0.0
    evidence = sample['evidence']
    contextual_evidence = sample['contextual_evidence']

    # Add sample information to the respective batch_objects.  
    batch_of_single_sentence_answers.append((claim, evidence))
    batch_of_contextual_answers.append((claim, contextual_evidence))
    batch_of_labels.append(label)
    batch_of_ids.append(id)

    if counter % batch_size == 0 : 
        
        # Batch representation object, that will be saved at the end. 
        batch_repr = {}

        # Get BERT representation for single sentence answers.
        tokens = tokenizer(batch_of_single_sentence_answers, return_tensors='tf', padding='max_length')
        repr = bert(tokens).last_hidden_state[:, 0, :].numpy()
        batch_repr['evidence_repr'] = repr


        # Get BERT representation for contextual answers. 
        tokens = tokenizer(batch_of_contextual_answers, return_tensors='tf', padding='max_length')
        repr = bert(tokens).last_hidden_state[:, 0, :].numpy()
        batch_repr['contextual_evidence_repr'] = repr

        # Prepare labels and IDs. IDs are for future QC purposes. 
        batch_repr['label'] = np.array(batch_of_labels)
        batch_repr['id'] = np.array(batch_of_ids)

        # Assertion checks to ensure there is no mismatches in preparing the batch.
        assert batch_repr['evidence_repr'].shape[0] == batch_repr['label'].shape[0]
        assert batch_repr['contextual_evidence_repr'].shape[0] == batch_repr['label'].shape[0]
        assert batch_repr['id'].shape[0] == batch_repr['label'].shape[0]

        # Save the BERT representation of the batch. 
        dest_path = os.path.join(data_dest_dir, '{}.npy'.format(counter))
        np.save(dest_path, batch_repr)


        # Save where each sample is stored, so that it can be retrieved (for QC)
        for id, label in zip(batch_of_ids, batch_of_labels) : 
            repr_info += '{},{},{}\n'.format(id, label, counter)
        with open('data/repr_info.csv', 'a+') as f : 
            f.write(repr_info)

        # Save counter, so in case the program restarts - last state can be recovered
        with open('configs/bert_repr_counter.txt', 'w') as f : 
            counter = f.write(str(counter))
        

        # Batch has been processed, reset batch lists. 
        batch_of_single_sentence_answers = []
        batch_of_contextual_answers = []
        batch_of_labels = []
        batch_of_ids = []

        print('Finished saving : {}/{} batches.'.format(counter/batch_size , int(num_samples/batch_size)))

    # Every nth iteration, log the status of the program. 
    if counter % log_frequency == 0 : 

        print('Finished processing {}/{} samples.'.format(counter+1, num_samples))
        print('Last {} samples took {} seconds.'.format(log_frequency , 
                                                        time.time() - batch_start_time))
        print('Time since the beginning of the program : ', time.time() - program_start_time)
        print('***---___---___---***')
        batch_start_time = time.time()


    counter += 1
