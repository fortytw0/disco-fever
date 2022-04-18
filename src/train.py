# Package Imports

import os
import glob
import time
import json
import numpy as np

#  Load config

with open('configs/train_config.json') as f : 
    train_config = json.load(f)

# Set Program Variables

build_model = train_config['build_model']
model_dir = train_config['model_dir']
train_data = train_config['train_data']
epochs  = train_config['epochs']

data_dir = 'data/repr/'
train_files = glob.glob(os.path.join(data_dir, '*.npy'))[:-2]
val_files = glob.glob(os.path.join(data_dir, '*.npy'))[-2:]

num_train_files = len(train_files)
num_val_files = len(val_files)

# Load Model

if build_model : 

    from src.utils.create_model import model
    model.summary()
    model.save(os.path.join(model_dir, train_data))

    train_config['build_model'] = False

    with open('configs/train_config.json' , 'w') as f : 
        json.dump(train_config, f)

else : 

    from tensorflow.keras.models import load_model
    model = load_model(os.path.join(model_dir, train_data))
    model.summary()


# Data Generator

def data_generator(split='train') : 

    if split=='train' : 
        files = train_files
    else : 
        files = val_files
    
    while True : 

        for f in files : 

            data = np.load(f, allow_pickle=True)[()]
            X = data[train_data]
            Y = data['label']
            yield X, Y


train_data_gen = data_generator(split='train')
val_data_gen = data_generator(split='val')

# Defining Callbacks

from tensorflow.keras import callbacks

model_ckpt = callbacks.ModelCheckpoint(os.path.join(model_dir, train_data))
csv_logger = callbacks.CSVLogger(os.path.join(model_dir, train_data+'.csv'), separator=',', append=False)
early_stopping = callbacks.EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Training Model 

from tensorflow.keras import optimizers, losses, metrics

model.compile(optimizer = optimizers.Adam(), 
            loss = losses.BinaryCrossentropy(),
            metrics = [metrics.Accuracy(), 
                        metrics.AUC(), 
                        metrics.TruePositives(),
                        metrics.TrueNegatives(),
                        metrics.FalsePositives(),
                        metrics.FalseNegatives()
                        ]
            )

model.fit(x=train_data_gen, 
        validation_data=val_data_gen,
        epochs=epochs, 
        callbacks=[model_ckpt, csv_logger, early_stopping], 
        steps_per_epoch=num_train_files,
        validation_steps=num_val_files,
        )




