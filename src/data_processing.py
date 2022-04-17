import json
import time

'''
Loading Data, Counter Files, Processed
'''

with open('data/pre-processed_samples.json') as f : 
    articles = json.load(f)

with open('configs/counter.txt') as f : 
    counter = int(f.read())


with open('data/processed_samples.json') as f : 
    processed_data = json.load(f)


'''
Set program variables.
'''

num_articles = len(articles)

save_frequency = 500
log_frequency = 500

max_num_supported = 10000
max_num_refuted = 10000

'''
Function Definition
'''

def process_sample(sample, id) : 

    processed = {'contextual_evidence' : '',
                'evidence' : ''}
    processed['id'] = id
    
    processed['label'] = sample['label']
    processed['claim'] = sample['claim']

    
    for title, lines in sample['evidence'].items() : 

        answer_index = title.split('_')[-1]
        prev_sentence_index = int(answer_index) - 1
        next_sentence_index = int(answer_index) + 1

        processed['evidence'] += lines[answer_index]

        if prev_sentence_index > 0 : 
            processed['contextual_evidence'] += lines[str(prev_sentence_index)] + ' '

        processed['contextual_evidence'] += lines[answer_index] + ' '

        if str(next_sentence_index) in lines: 
            processed['contextual_evidence'] += lines[str(next_sentence_index)] + '\n'
    
    return processed


'''
Main : 

For each article, extract evidence pair and save it.

'''

num_supported = 0
num_refuted = 0 

program_start_time = time.time()
batch_start_time = time.time()

while counter < num_articles : 

    sample = articles[counter]

    if (sample['label'] == 'SUPPORTS') and (num_supported < max_num_supported) : 
        num_supported += 1
        processed_data.append(process_sample(sample, counter))

    elif (sample['label'] == 'REFUTES') and (num_refuted < max_num_refuted) : 
        num_refuted += 1
        processed_data.append(process_sample(sample, counter))

    if counter % save_frequency == 0 :

        with open('data/processed_samples.json', 'w') as f : 
            json.dump(processed_data , f)

        with open('configs/counter.txt', 'w') as f : 
            f.write(str(counter))

        print('Processed data saved at iteration : ' , counter)

    if counter % log_frequency == 0 : 

        print('Finished processing {}/{} samples.'.format(counter+1, num_articles))
        print('Last {} samples took {} seconds.'.format(log_frequency , 
                                                        time.time() - batch_start_time))
        print('Total number of supported evidence : ' , num_supported)
        print('Total number of refuted evidence : ', num_refuted)
        print('Time since the beginning of the program : ', time.time() - program_start_time)
        print('***---___---___---***')
        batch_start_time = time.time()



    counter += 1
        

    



    
    

    


            








    









