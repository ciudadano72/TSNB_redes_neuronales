import nas
import lib_nas 

# _bias_2_4 v1 --Check local 
# Estructura de polarizacion 1/2 Byte --caso de uso practico (3)
# @autor:Jose Luis Prado Seoane ---IT Security Researcher & Developer
#
# Research: Teoria de Sistemas Neuronales (I.A) --TSNB 
# Redes Neuronales y su convergencia hacia modelos e implementaciones orientadas a la
# Ciberseguridad

class _bias_2_4(): # @estructura _bias_01_net
    #CONSTRUCTOR:
    def __init__(self,_bias_):
      self.debug=1
      if self.debug==1:
        print"\n"
        print"";print ("Ejecutando " + self.__class__.__name__) + "..."
        self.__neuron=nas.neuron(int(_bias_))
        self.__bias=int(_bias_)

    def _memory_pattern_(self,_dendrite_0_,_dendrite_1_,_pattern_):
        self._layer_1_1_(self.__neuron,self.__bias,self._memory_(self.__bias))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        _rtn = self._pattern_nas(_dendrite_0_,_dendrite_1_,self.__neuron._out_,_pattern_)
        self._layer_1_1_(self.__neuron,self.__bias,self._memory_(_rtn))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        return self.__neuron._out_
        self._layer_1_1_(self.__neuron,self.__bias,self._memory_(self.__bias))
    
    def _layer_1_1_(self,_neuron,_idnas,_learn):
        def neuron_0():
            _neuron.rst_sign_();_neuron.ibn_(0,0,int(_learn[0]));_neuron.ibn_(0,1,int(_learn[1]))
            _neuron.ibn_(1,0,int(_learn[2]));_neuron.ibn_(1,1,int(_learn[3]))
        __rst_sign = {0 : neuron_0,}
        __rst_sign [int(_idnas)]()

    def _memory_(self,id_mode):
        def s0():global _learn;_learn=[0,0,0,1]
        def s1():global _learn;_learn=[1,1,1,0]
        def s2():global _learn;_learn=[0,1,1,1]
        def s3():global _learn;_learn=[1,0,0,0]
        def s4():global _learn;_learn=[0,1,1,0] 
        def s5():global _learn;_learn=[1,0,0,1]
        __learn = {0 : s0,1 : s1,2 : s2,3 : s3,4 : s4,5 : s5,}
        __learn [int(id_mode)]()
        return _learn
    
    def _pattern_nas(self,__dendrite_0,__dendrite_1,_out_nas,_pattern):
        _bin_ = str(bin(__dendrite_0) + bin(__dendrite_1)) 
        _mem_ = (_bin_[2] + _bin_[5]) 
        def s_00():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[0])) != 0] 
        def s_01():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[1])) != 0]
        def s_10():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[2])) != 0]
        def s_11():global _balancer_; _balancer_ = (0,1)[cmp(_out_nas,int(_pattern[3])) != 0]
        __balancer = {"00" : s_00,"01" : s_01,"10" : s_10,"11" : s_11,};__balancer [_mem_]()
        return _balancer_

# (Parte estructura:Clase _bias_01_net (bias2.4.py)
# // Caso de uso (3) : Implementacion....
def _init_net_2_():
    n0=_bias_2_4(0)
    while True:
        _pattern=raw_input ('PATRON DESEADO: ')
        for x in range(4):
            den_0_io= int(raw_input ('den_0: '))
            den_1_io= int(raw_input ('den_1: '))
            neuron_out=n0._memory_pattern_(den_0_io,den_1_io,_pattern)
            print "------------------> %s" %neuron_out
_init_net_2_()
