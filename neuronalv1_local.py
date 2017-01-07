#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import nas

#func_memory
def _memory_(id_mode):
    def s0():global _learn_;i0=0;i1=0;i2=0;i3=1;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #AND
    def s1():global _learn_;i0=1;i1=1;i2=1;i3=0;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #NAND
    def s2():global _learn_;i0=0;i1=1;i2=1;i3=1;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #OR
    def s3():global _learn_;i0=1;i1=0;i2=0;i3=0;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #NOR
    def s4():global _learn_;i0=0;i1=1;i2=1;i3=0;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #XOR
    def s5():global _learn_;i0=1;i1=0;i2=0;i3=1;_learn_= str(i0) + str(i1) + str(i2) + str(i3) #XNOR
    __learn = {0 : s0,1 : s1,2 : s2,3 : s3,4 : s4,5 : s5,};__learn [int(id_mode)]()
    return _learn_

#Layer neuronal -0- In
#----------------------------------------------------------------------------------------------------------------------------------------------------------
n0 = nas.neuron(0);n1 = nas.neuron(1);n2 = nas.neuron(2);n3 = nas.neuron(3)
def layer_0(id_nas,_learn_):
    def neuron_0():n0.rst_sign_();n0.ibn_(0,0,int(_learn_[0]));n0.ibn_(0,1,int(_learn_[1]));n0.ibn_(1,0,int(_learn_[2]));n0.ibn_(1,1,int(_learn_[3]))
    def neuron_1():n1.rst_sign_();n1.ibn_(0,0,int(_learn_[0]));n1.ibn_(0,1,int(_learn_[1]));n1.ibn_(1,0,int(_learn_[2]));n1.ibn_(1,1,int(_learn_[3]))
    def neuron_2():n2.rst_sign_();n2.ibn_(0,0,int(_learn_[0]));n2.ibn_(0,1,int(_learn_[1]));n2.ibn_(1,0,int(_learn_[2]));n2.ibn_(1,1,int(_learn_[3]))
    def neuron_3():n3.rst_sign_();n3.ibn_(0,0,int(_learn_[0]));n3.ibn_(0,1,int(_learn_[1]));n3.ibn_(1,0,int(_learn_[2]));n3.ibn_(1,1,int(_learn_[3]))
    __rst_sign = {0 : neuron_0,1 : neuron_1,2 : neuron_2,3 : neuron_3,}
    __rst_sign [int(id_nas)]()

#Layer neuronal -1-
#----------------------------------------------------------------------------------------------------------------------------------------------------------
n4 = nas.neuron(4);n41 = nas.neuron(41);n42 = nas.neuron(42);n5 = nas.neuron(5);n51 = nas.neuron(51);n52 = nas.neuron(52)
n6 = nas.neuron(6);n61 = nas.neuron(61);n62 = nas.neuron(62)
def layer_1(id_nas,_learn_):
    def neuron_4():n4.rst_sign_();n4.ibn_(0,0,int(_learn_[0]));n4.ibn_(0,1,int(_learn_[1]));n4.ibn_(1,0,int(_learn_[2]));n4.ibn_(1,1,int(_learn_[3]))
    def neuron_41():n41.rst_sign_();n41.ibn_(0,0,int(_learn_[0]));n41.ibn_(0,1,int(_learn_[1]));n41.ibn_(1,0,int(_learn_[2]));n41.ibn_(1,1,int(_learn_[3]))
    def neuron_42():n42.rst_sign_();n42.ibn_(0,0,int(_learn_[0]));n42.ibn_(0,1,int(_learn_[1]));n42.ibn_(1,0,int(_learn_[2]));n42.ibn_(1,1,int(_learn_[3]))
    def neuron_5():n5.rst_sign_();n5.ibn_(0,0,int(_learn_[0]));n5.ibn_(0,1,int(_learn_[1]));n5.ibn_(1,0,int(_learn_[2]));n5.ibn_(1,1,int(_learn_[3]))
    def neuron_51():n51.rst_sign_();n51.ibn_(0,0,int(_learn_[0]));n51.ibn_(0,1,int(_learn_[1]));n51.ibn_(1,0,int(_learn_[2]));n51.ibn_(1,1,int(_learn_[3]))
    def neuron_52():n52.rst_sign_();n52.ibn_(0,0,int(_learn_[0]));n52.ibn_(0,1,int(_learn_[1]));n52.ibn_(1,0,int(_learn_[2]));n52.ibn_(1,1,int(_learn_[3]))
    def neuron_6():n6.rst_sign_();n6.ibn_(0,0,int(_learn_[0]));n6.ibn_(0,1,int(_learn_[1]));n6.ibn_(1,0,int(_learn_[2]));n6.ibn_(1,1,int(_learn_[3]))
    def neuron_61():n61.rst_sign_();n61.ibn_(0,0,int(_learn_[0]));n61.ibn_(0,1,int(_learn_[1]));n61.ibn_(1,0,int(_learn_[2]));n61.ibn_(1,1,int(_learn_[3]))
    def neuron_62():n62.rst_sign_();n62.ibn_(0,0,int(_learn_[0]));n62.ibn_(0,1,int(_learn_[1]));n62.ibn_(1,0,int(_learn_[2]));n62.ibn_(1,1,int(_learn_[3]))
    __rst_sign = {4 : neuron_4,41 : neuron_41,42 : neuron_42,5 : neuron_5,51 : neuron_51,52 : neuron_52,6 : neuron_6,61 : neuron_61,62 : neuron_62,}
    __rst_sign [int(id_nas)]()

#Layer neuronal -2- Out
#----------------------------------------------------------------------------------------------------------------------------------------------------------
n7 = nas.neuron(7);n71 = nas.neuron(71)
def layer_2(id_nas,_learn_):
    def neuron_7():n7.rst_sign_();n7.ibn_(0,0,int(_learn_[0]));n7.ibn_(0,1,int(_learn_[1]));n7.ibn_(1,0,int(_learn_[2]));n7.ibn_(1,1,int(_learn_[3]))
    def neuron_71():n71.rst_sign_();n71.ibn_(0,0,int(_learn_[0]));n71.ibn_(0,1,int(_learn_[1]));n71.ibn_(1,0,int(_learn_[2]));n71.ibn_(1,1,int(_learn_[3]))
    __rst_sign = {7 : neuron_7,71 : neuron_71,}
    __rst_sign [int(id_nas)]()

def __init_net():
    # Layer -0-
    layer_0(0,_memory_(0));layer_0(1,_memory_(0));layer_0(2,_memory_(0));layer_0(3,_memory_(0))
    # Layer -1-
    layer_1(4,_memory_(0));layer_1(41,_memory_(0));layer_1(42,_memory_(0))
    layer_1(5,_memory_(0));layer_1(51,_memory_(0));layer_1(52,_memory_(0))
    layer_1(6,_memory_(0));layer_1(61,_memory_(0));layer_1(62,_memory_(0))
    # Layer -2-
    layer_2(7,_memory_(0));layer_2(71,_memory_(0))

    # Netlist
    A=1;B=1
    n0.ibn_(A,B);n1.ibn_(A,B);n2.ibn_(A,B);n3.ibn_(A,B); # Net_layer -0-
    n4.ibn_(n0._out_,n1._out_);n41.ibn_(n4._out_,n2._out_);n42.ibn_(n41._out_,n3._out_) # Net_layer -1-
    n5.ibn_(n0._out_,n1._out_);n51.ibn_(n5._out_,n2._out_);n52.ibn_(n51._out_,n3._out_) # Net_layer -1-
    n6.ibn_(n0._out_,n1._out_);n61.ibn_(n6._out_,n2._out_);n62.ibn_(n61._out_,n3._out_) # Net_layer -1-
    n7.ibn_(n42._out_,n52._out_);n71.ibn_(n7._out_,n62._out_)# Net_layer -2-
    print n71._out_
__init_net()
