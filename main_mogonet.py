""" Example for MOGONET classification """
from train_test import train_test

def run(patient_data):
    """Run MOGONET classification with the given patient data."""
    # Configure parameters for MOGONET
    data_folder = 'ROSMAP'
    view_list = [1, 2, 3]
    num_epoch_pretrain = 500
    num_epoch = 2500
    lr_e_pretrain = 1e-3
    lr_e = 5e-4
    lr_c = 1e-3

    # Set number of classes based on data folder
    if data_folder == 'ROSMAP':
        num_class = 2
    elif data_folder == 'BRCA':
        num_class = 5

    # Call train_test to process data (modify this based on your logic)
    more_common_class, accuracy = train_test(data_folder, view_list, num_class,
                                  lr_e_pretrain, lr_e, lr_c, 
                                  num_epoch_pretrain, num_epoch)

    # Return the classification result (or adapt to your use case)
    return {"prediction_list": more_common_class, "accuracy": accuracy}
