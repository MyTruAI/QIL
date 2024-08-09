import numpy as np

def normalize_data(data):
    """
    Normalize the data to a range between 0 and 1.

    Parameters:
    - data: A numpy array or a list of numerical values.

    Returns:
    - normalized_data: A numpy array with values normalized between 0 and 1.
    """
    data = np.array(data)
    normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))
    return normalized_data

def encode_state(state):
    """
    Encode a state as a binary string.

    Parameters:
    - state: A list or array of integers or binary values representing the state.

    Returns:
    - encoded_state: A binary string representing the state.
    """
    return ''.join(format(x, 'b').zfill(8) for x in state)

def decode_binary(binary_string):
    """
    Decode a binary string back into a list of integers.

    Parameters:
    - binary_string: A string representing binary values.

    Returns:
    - decoded_values: A list of integers decoded from the binary string.
    """
    byte_size = 8
    decoded_values = [int(binary_string[i:i+byte_size], 2) for i in range(0, len(binary_string), byte_size)]
    return decoded_values

def calculate_reward(context_value, impact_value):
    """
    Calculate a reward based on context and impact values.

    Parameters:
    - context_value: A numerical value representing the context.
    - impact_value: A numerical value representing the impact.

    Returns:
    - reward: A computed reward value.
    """
    reward = context_value + impact_value
    return reward

def softmax(x):
    """
    Compute the softmax of a vector.

    Parameters:
    - x: A numpy array or list of values.

    Returns:
    - softmax_values: A numpy array with the softmax values.
    """
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def one_hot_encode(labels, num_classes):
    """
    One-hot encode a list of labels.

    Parameters:
    - labels: A list of numerical labels.
    - num_classes: The total number of classes.

    Returns:
    - one_hot_encoded: A numpy array representing one-hot encoded labels.
    """
    one_hot_encoded = np.zeros((len(labels), num_classes))
    one_hot_encoded[np.arange(len(labels)), labels] = 1
    return one_hot_encoded
