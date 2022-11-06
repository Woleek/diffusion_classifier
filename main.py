from model_lightning import LitModel
from tests import predict_labels

import torch
from pytorch_lightning import Trainer

if __name__ == '__main__':
    input_size = 2
    sequence_length = 300
    hidden_size = 300
    num_classes = 5
    num_layers = 2
    batches = {'train_bs': 100, 'val_bs': 100, 'test_bs': 100}
    
    num_epochs = 10
    logs_dir = 'gru_logs/'

    model = LitModel(num_layers, hidden_size, input_size, num_classes, batches)

    trainer = Trainer(max_epochs=num_epochs,
                      fast_dev_run=False,
                      auto_lr_find=True,
                      log_every_n_steps=50,
                      default_root_dir=logs_dir,
                      )
    trainer.fit(model)
    
    torch.save(model.state_dict(), "GRU.pt")
    
    predict_labels(model)