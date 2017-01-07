
import nas
#import Lib_NAS_Rnas_IA_

#lib_nas.py --simple v.2.0
#libreria Neuronal basica --Lib 
# ---PARTE PARCIAL:01/0001/2011 --Pertene a libreria: Lib_NAS_Rnas_IA_ (460 funciones)
# -----Lib_NAS_Rnas_IA_ :ROOT
#         |
#         +.........Lib_Nas.py
#         |
#         +... (+) 459 Func(): dinamicas/estaticas:BAMS:EOF_id:Semaforos:Bypass .... 
#         
# @autor:Jose Luis Prado Seoane ---IT Security Researcher & Developer
# @_ciudadano72 ---Follow_me
#
# Research: Teoria de Sistemas Neuronales (I.A) --TSNB 808565016
# Redes Neuronales y su convergencia hacia modelos e implementaciones orientadas a la
# Ciberseguridad

# Descripcion: **********************************************************************************
# Libreria Neuronal basica (lib_nas) para la conformacion estrucrural de redes tipo arbol 
# simetricas no orientadas.Esta libreria esta incluida en la libreria estructural de topologias
# Lib_NAS_Rnas_IA_, que incluye todas las principales topologias de Redes Neuronales que se 
# presentan en este Research teorico-practico.
#
# NOTA: Esta presentacion via Web es parcial a la totalidad de la libreria lib_nas. Solo se iran
# liberando publicamente aquellas func() necesarias para la implementacion de los casos practicos
# de uso que se presentaran.  

def _layer_1_1_(_neuron,_idnas,_learn):
    def neuron_0():
        _neuron.rst_sign_();_neuron.ibn_(0,0,int(_learn[0]));_neuron.ibn_(0,1,int(_learn[1]))
        _neuron.ibn_(1,0,int(_learn[2]));_neuron.ibn_(1,1,int(_learn[3]))
    __rst_sign = {0 : neuron_0,}
    __rst_sign [int(_idnas)]()

#Capa neuronal -2 neuronas-
n1 = nas.neuron(1);n2 = nas.neuron(2)
def _layer_2_1(id_nas,_learn_):
    def neuron_1():n1.rst_sign_();n1.ibn_(0,0,int(_learn_[0]));n1.ibn_(0,1,int(_learn_[1]));
    n1.ibn_(1,0,int(_learn_[2]));n1.ibn_(1,1,int(_learn_[3]))
    def neuron_2():n2.rst_sign_();n2.ibn_(0,0,int(_learn_[0]));n2.ibn_(0,1,int(_learn_[1]));
    n2.ibn_(1,0,int(_learn_[2]));n2.ibn_(1,1,int(_learn_[3]))
    __rst_sign = {1 : neuron_1,2 : neuron_2,}
    __rst_sign [int(id_nas)]()

#Capa neuronal -3 neuronas-
n3 = nas.neuron(3);n4 = nas.neuron(4);n5 = nas.neuron(5)
def _layer_3_1(id_nas,_learn_):
    def neuron_3():n3.rst_sign_();n3.ibn_(0,0,int(_learn_[0]));n3.ibn_(0,1,int(_learn_[1]));
    n3.ibn_(1,0,int(_learn_[2]));n3.ibn_(1,1,int(_learn_[3]))
    def neuron_4():n4.rst_sign_();n4.ibn_(0,0,int(_learn_[0]));n4.ibn_(0,1,int(_learn_[1]));
    n4.ibn_(1,0,int(_learn_[2]));n4.ibn_(1,1,int(_learn_[3]))
    def neuron_5():n5.rst_sign_();n5.ibn_(0,0,int(_learn_[0]));n5.ibn_(0,1,int(_learn_[1]));
    n5.ibn_(1,0,int(_learn_[2]));n5_1.ibn_(1,1,int(_learn_[3]))
    __rst_sign = {3 : neuron_3,4 : neuron_4,5 : neuron_5,}
    __rst_sign [int(id_nas)]()

#Balanceador neuronal de funci0n -6 modos-
def _memory_(id_mode):
    def s0():global _learn;_learn=[0,0,0,1]
    def s1():global _learn;_learn=[1,1,1,0]
    def s2():global _learn;_learn=[0,1,1,1]
    def s3():global _learn;_learn=[1,0,0,0]
    def s4():global _learn;_learn=[0,1,1,0] 
    def s5():global _learn;_learn=[1,0,0,1]
    __learn = {0 : s0,1 : s1,2 : s2,3 : s3,4 : s4,5 : s5,}
    __learn [int(id_mode)]()
    return _learn

#correlador neuronal
def _correlator(_binary_pattern_):
    tokens=[];secuencia=""
    for token in _binary_pattern_:
        tokens.append(int(token))
    print tokens
    for x in range(len(tokens)):
        if x<10:
            if tokens[x]==1:secuencia=secuencia+str(x)
        else:
            if tokens[x]==1:secuencia=secuencia+"["+str(x)
    return secuencia

#Balanceador neuronal de aprendizaje -4 estados-
def _pattern_nas(__dendrite_0,__dendrite_1,_out_nas,_pattern):
    _bin_ = str(bin(__dendrite_0) + bin(__dendrite_1)) 
    _mem_ = (_bin_[2] + _bin_[5])
    def s_00():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[0])) != 0] 
    def s_01():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[1])) != 0]
    def s_10():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[2])) != 0]
    def s_11():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[3])) != 0]
    __balancer = {"00" : s_00,"01" : s_01,"10" : s_10,"11" : s_11,};__balancer [_mem_]()
    return _balancer_

#Balanceador neuronal de aprendizaje -16 estados-
def _pattern_nas_16(__dendrite_0,__dendrite_1,__dendrite_2,__dendrite_3,_out_nas,_pattern):
    _bin_ = str(bin(__dendrite_0)+bin(__dendrite_1)+bin(__dendrite_2)+bin(__dendrite_3)) 
    _mem_=(_bin_[2]+_bin_[5]+_bin_[8]+_bin_[11]) 
    def s_0000():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[0])) != 0] 
    def s_0001():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[1])) != 0]
    def s_0010():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[2])) != 0]
    def s_0011():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[3])) != 0]
    def s_0100():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[4])) != 0] 
    def s_0101():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[5])) != 0]
    def s_0110():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[6])) != 0]
    def s_0111():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[7])) != 0]
    def s_1000():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[8])) != 0] 
    def s_1001():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[9])) != 0]
    def s_1010():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[10])) != 0]
    def s_1011():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[11])) != 0]
    def s_1100():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[12])) != 0] 
    def s_1101():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[13])) != 0]
    def s_1110():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[14])) != 0]
    def s_1111():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[15])) != 0]
    __balancer = {"0000" : s_0000,"0001" : s_0001,"0010" : s_0010,"0011" : s_0011,
                  "0100" : s_0100,"0101" : s_0101,"0110" : s_0110,"0111" : s_0111,
                  "1000" : s_1000,"1001" : s_1001,"1010" : s_1010,"1011" : s_1011,
                  "1100" : s_1100,"1101" : s_1101,"1110" : s_1110,"1111" : s_1111,}
    __balancer [_mem_]()
    return _balancer_
