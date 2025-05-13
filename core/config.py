import os

# Suppress TensorFlow warnings during prediction
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # 0=all messages, 1=no INFO, 2=no WARNING, 3=no ERROR

# Configure GPU memory growth to prevent using all GPU memory
def configure_gpu():
    import tensorflow as tf
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                # Set memory growth - this allocates memory as needed instead of claiming all at once
                tf.config.experimental.set_memory_growth(gpu, True)
                
                # Alternative approach: set a memory limit (e.g., 2GB)
                # tf.config.experimental.set_virtual_device_configuration(
                #     gpu,
                #     [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=2048)]  # 2GB limit
                # )
            print("✅ GPU memory growth enabled successfully")
        except RuntimeError as e:
            print(f"❌ Error setting GPU memory growth: {e}")
    return tf

# Constants
TIME_STEPS = 90  # Adjust this value according to your model's requirements
MODEL_PATH = "models/final_lstm_model.h5"