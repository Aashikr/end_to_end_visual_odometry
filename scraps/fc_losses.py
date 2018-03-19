import tensorflow as tf


def fc_losses(outputs, labels_u):
    diff_u = outputs[:, :, 0:6] - labels_u
    L = outputs[:, :, 6:12]

    # The network outputs Q=LL* through the Cholesky decomposition,
    # we assume L is diagonal, Q is always psd
    Q = tf.multiply(L, L)

    # determinant of a diagonal matrix is product of it diagonal
    det_Q = tf.reduce_prod(Q, axis=2)

    # inverse of a diagonal matrix is elemental inverse
    inv_Q = tf.div(tf.constant(1, dtype=tf.float32), Q)

    # sum of determinants along the time
    sum_det_Q = tf.reduce_sum(Q, axis=1)

    # sum of diff_u' * inv_Q * diff_u
    s = tf.reduce_sum(tf.multiply(diff_u, tf.multiply(inv_Q, diff_u)), axis=(1,2,))

    # add and multiplies of sum by 1 / t
    loss = (s + sum_det_Q) / tf.cast(tf.shape(outputs)[1], tf.float32)

    return tf.reduce_mean(loss)

# outputs = tf.constant([
#     [[1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 2]],
#     [[0, 0, 0, 0, 0, 0, 0], [2, 0, 1, 0, 0, 2, 0]]
# ], dtype=tf.float32)
#
# labels = tf.constant([
#     [[8, 9, 10, 11, 12, 13, 14], [1, 2, 1, 1, 1, 1, 1]],
#     [[0, 2, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
# ], dtype=tf.float32)
# se3_losses(outputs, labels, 0)