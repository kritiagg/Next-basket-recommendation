
RAW_DATA_DIR = '../Instacart/raw/'
FEAT_DATA_DIR = '../Instacart/feat/'
DREAM_MODEL_DIR = '../Instacart/dream/'

DREAM_CONFIG = {'basket_pool_type': 'max', # 'avg'
                'rnn_layers': 1, # 2, 3
                'rnn_type': 'LSTM',#'RNN_TANH',#'GRU',#'LSTM',# 'RNN_RELU',
                'dropout': 0.5,
                # 'num_product': 49688 + 1, # padding idx = 0
                'num_product': 49688 + 1 + 1, 
                # 49688 products, padding idx = 0, none idx = 49689, none idx indicates no products
                'none_idx': 49689,
                'embedding_dim': 64, # 128 
                'cuda': False, # True,
                'clip': 20, # 0.25
                'epochs': 100,
                'batch_size': 4, #256
                'learning_rate': 0.01, # 0.0001
                'log_interval': 1, # num of batchs between two logging
                'checkpoint_dir': DREAM_MODEL_DIR + 'reorder-next-dream-{epoch:02d}-{loss:.4f}.model',
                }