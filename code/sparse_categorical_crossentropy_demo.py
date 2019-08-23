def test19():
    y2 = tf.convert_to_tensor([[0, 0, 1, 0]], dtype=tf.int64)

    y_2 = tf.convert_to_tensor([[-2.6, -1.7, 3.2, 0.1]], dtype=tf.float32)
    print(tf.argmax(y2, 1))
    c2 = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y_2, labels= tf.argmax(y2, 1))

    c3 =  K.sparse_categorical_crossentropy(tf.argmax(y2, 1), y_2) # target and output 

    print(c2)
    print(c3)

