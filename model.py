# import the required libraries 
import tensorflow as tf

#function for take the processed audio and return the class name
def DetectSound(sound):
    # path 
    model_path=r"C:\YusrGP\YusrProject\AudioDyslexia\final"
    export = tf.saved_model.load(model_path)
    res = export(tf.constant(sound))
    class_names = res['class_names']
    class_name = class_names.numpy()[0].decode("utf-8")
    return class_name
# file_path = r'D:/Audio_project/YusrProject/AudioDyslexia/test/kaf/kaf.wav'

