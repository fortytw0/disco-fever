from tensorflow.keras import layers, Input, Model



input_layer = Input(shape=(768, ))
dense = layers.Dense(256, 'relu')(input_layer)
dense = layers.Dense(128, 'relu')(dense)
dense = layers.Dense(64, 'relu')(dense)
output_layer = layers.Dense(1, 'sigmoid')(dense)

model = Model(inputs=input_layer, outputs=output_layer)


