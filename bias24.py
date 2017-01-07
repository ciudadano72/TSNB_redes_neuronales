
import nas
import sys
import lib_nas
#import Lib_NAS_Rnas_IA_

# _bias_2_4 v2.0
# estructura Neuronal 2 bits --4 patrones de adaptacion 
#       
# @autor:Jose Luis Prado Seoane ---IT Security Researcher & Developer
#
# Research: Teoria de Sistemas Neuronales (I.A) --TSNB 808565016
# Redes Neuronales y su convergencia hacia modelos e implementaciones orientadas a la
# Ciberseguridad

# Descripcion: **********************************************************************************
# Estructura neuronal adaptativa de 2 bits dimensional de (1)-->(n+1) patrones variables en los 
# imputs. El secuenciador es externo a la propia estructura y establece un Netlist para poder
# integrarla en un cumulo adjunto dentro de una area de datos en deteccion de patrones***********
#
# ------RNA------<>
#          { |
#          { |+++++(estructura_0:bias:semaforos:BAMS:correladores...)
#          { |      |
#          { |      |++++++(neuron_0 + neuron_(n+1):NETLIST) 
#          { |
#          { |+++++(estructura_(n+1)..
#          { 
#          { : CUMULO/S 

# @info:
# @estructura: Clase -- 2 Bits : 4 pattern detected 
# @info: La estructura neuronal no se depura por codigo, depurador externo via @tokens
class _bias_2_4(): # @estructura _bias_01_net
    #CONSTRUCTOR:
    def __init__(self,_bias_):
      self.debug=1
      if self.debug==1:
        print"";print ("Ejecutando " + self.__class__.__name__) + "...\n"
        self.__neuron=nas.neuron(_bias_)
        self.__bias=int(_bias_)
        self.__base_pattern=[]
        for base_pattern in range(4):
            self.__base_pattern.append(0)

    # @info: Pattern imputs --cor
    def _memory_pattern_(self,_dendrite_0_,_dendrite_1_,_pattern_):
        pattern=[]
        self._set_(pattern,_pattern_)
        lib_nas._layer_1_1_(self.__neuron,self.__bias,lib_nas._memory_(self.__bias))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        _rtn = lib_nas._pattern_nas(_dendrite_0_,_dendrite_1_,self.__neuron._out_,self.__base_pattern)
        lib_nas._layer_1_1_(self.__neuron,self.__bias,lib_nas._memory_(_rtn))
        self.__neuron.ibn_(_dendrite_0_,_dendrite_1_)
        return self.__neuron._out_
        lib_nas._layer_1_1_(self.__neuron,self.__bias,lib_nas._memory_(self.__bias))

    # @info: mapa de adaptacion
    def _mapper_(self,_pattern_):
        valores=[0,1];mapa=[];pattern=[]
        print "";print "<--mapper-->";print "2 inputs:4 pattern"
        self._set_(pattern,_pattern_)
        for x in valores:
            for y in valores:
                mapa.append("%s%s" %(x,y))
        for x in range(len(mapa)):
            print "(%s)---%s:->%s" %(x,mapa[x],self.__base_pattern[x])
        print ""

    # @info: Reseat volcados y _memory_pattern
    def _set_(self,pattern,_pattern_):
        for token in range(len(self.__base_pattern)):self.__base_pattern[token]=0
        for token in _pattern_:pattern.append(int(token))
        for token in pattern: self.__base_pattern[token]=1

#--------------------------------------------------------------------------------app()
# @info: app_local
def _init_net_3_(_bias_):
    n0 = _bias_2_4(_bias_)
    while True:
        try:
            _pattern=raw_input ('PATRON DESEADO: ')
            if _pattern==":q":
                break
                sys.exit(-1)
            if len(_pattern)==4:
                learning=lib_nas._correlator(_pattern)
                n0._mapper_(learning)
                for x in range(4):
                    den_0_io= int(raw_input ('den_0: '))
                    den_1_io= int(raw_input ('den_1: '))
                    neuron_out=n0._memory_pattern_(den_0_io,den_1_io,learning)
                    print "------------------> %s" %neuron_out
            else:
                print "Patron de aprendizaje Bias : 4 tokens ej.- 0101"
        except:
            print "Parametro de aprendizaje incorrecto Bias"

_init_net_3_(0)

# @info: app_local
def _init_net_2_(_bias_):
    n0 = _bias_2_4(_bias_)
    while True:
        try:
            _pattern=raw_input ('PATRON DESEADO: ')
            if _pattern==":q":
                break
                sys.exit(-1)
            if len(_pattern)<=4:
                n0._mapper_(_pattern)
                for x in range(4):
                    den_0_io= int(raw_input ('den_0: '))
                    den_1_io= int(raw_input ('den_1: '))
                    neuron_out=n0._memory_pattern_(den_0_io,den_1_io,_pattern)
                    print "------------------> %s" %neuron_out
            else:
                print "Maximo patron de aprendizaje Bias : 4 tokens"
        except:
            print "Parametro de aprendizaje incorrecto Bias:0123"

#_init_net_2_(0)
