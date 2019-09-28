'''
File name: quaternion_toolbox.py
Created by: Mike Bernard
Creator email: mike.bernard@uconn.edu
Creation date: 2019-09-28

Python version: 3.7.3

Tools for dealing with scalar-first, transform, unit,
right quaternions with Malcolm Shuster's conventions.
'''

from numpy import array, cross, dot, concatenate
from numpy.linalg import norm


def qcomp(q1, q2):
    '''
    Compose two quaternions.
    '''
    q1s = q1[3]
    q1v = array(q1[0:3])
    q2s = q2[3]
    q2v = array(q2[0:3])

    v = q1s*q2v + q2s*q1v - cross(q1v, q2v)
    s = array([q1s*q2s - dot(q2v, q1v)])

    return concatenate([v, s])


def qnorm(q):
    '''
    Normalize a quaternion.
    '''
    return q/norm(q)


def qvectransform(q, v):
    '''
    Transform a vector's frame.
    '''
    qvec = concatenate([v, array([0])])
    transformed = qcomp(q, qcomp(qvec, qconjugate(q)))
    return transformed[0:3]


def qconjugate(q):
    '''
    Get the conjugate of a quaternion. This is equal to
    the inverse for unit quaternions.
    '''
    return concatenate([-1*q[0:3], q[3]])
