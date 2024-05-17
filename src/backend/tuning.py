from model import Net
import training as training
import torch

def tune_lr():
  lr_choices = {0.001: 0, 0.01: 0, 0.05: 0, 0.1: 0}
  for c in lr_choices:
    train_data, val_data = training.get_data()
    model = Net()
    training.train(model, train_data, epochs = 20, lr = c)
    result = training.test(model, val_data)
    lr_choices[c] = result
  print("The optimal learning rate is " + str(max(lr_choices, key = lambda x: lr_choices[x])))

def tune_epochs():
  epoch_choices = {5: 0, 10: 0, 15: 0, 20: 0, 25:0}
  for c in epoch_choices:
    train_data, val_data = training.get_data()
    model = Net()
    training.train(model, train_data, epochs = c)
    result = training.test(model, val_data)
    epoch_choices[c] = result
  print("The optimal epoch size is " + str(max(epoch_choices, key = lambda x: epoch_choices[x])))



if __name__ == "__main__":
    tune_lr()
    #tune_epochs()

