import nas
import sys
import lib_nas 
#import Lib_NAS_Rnas_IA_

# _bias_4_16 v3.0
# estructura Neuronal 4 bits --16 patrones de adaptacion 
#       
# @autor:Jose Luis Prado Seoane ---IT Security Researcher & Developer
#
# Research: Teoria de Sistemas Neuronales (I.A) --TSNB 808565016
# Redes Neuronales y su convergencia hacia modelos e implementaciones orientadas a la
# Ciberseguridad

# Descripcion: **********************************************************************************
# Estructura neuronal adaptativa de 4 bits dimensional de (1)-->(n+1) patrones variables en los 
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

# @estructura: Clase -- 4 Bits : 16 pattern detected 
# @info: La estructura neuronal no se depura por codigo, depurador externo via @tokens
class _bias_4_16(): # @estructura _bias_02_net
    #CONSTRUCTOR:
    def __init__(self,_bias_):
      self.debug=1
      if self.debug==1:
        print"";print ("Ejecutando " + self.__class__.__name__) + "...\n"
        self.__neuron_0=nas.neuron(_bias_)
        self.__neuron_1=nas.neuron(_bias_)
        self.__neuron_2=nas.neuron(_bias_)
        self.__bias=int(_bias_)
        self.__base_pattern=[]
        for base_pattern in range(16):
            self.__base_pattern.append(0)

    # @info: Pattern imputs --core
    def _memory_pattern_(self,_dendrite_0_,_dendrite_1_,_dendrite_2_,_dendrite_3_,_pattern_):
        pattern=[]
        self._set_(pattern,_pattern_)
        self._memory_init_0()
        self.__neuron_0.ibn_(_dendrite_0_,_dendrite_1_)
        self.__neuron_1.ibn_(_dendrite_2_,_dendrite_3_)
        self.__neuron_2.ibn_(self.__neuron_0._out_,self.__neuron_1._out_)
        _rtn = lib_nas._pattern_nas_16(_dendrite_0_,_dendrite_1_,_dendrite_2_,_dendrite_3_,self.__neuron_2._out_,self.__base_pattern)
        lib_nas._layer_1_1_(self.__neuron_2,self.__bias,lib_nas._memory_(_rtn))
        self.__neuron_2.ibn_(self.__neuron_0._out_,self.__neuron_1._out_)
        return self.__neuron_2._out_
        self._memory_init_0()
    
    # @info: mapa de adaptacion
    def _mapper_(self,_pattern_):
        valores=[0,1];mapa=[];pattern=[];count=0
        print "";print "<--mapper-->";print "2 inputs:4 pattern"
        self._set_(pattern,_pattern_)
        for x in valores:
            for y in valores:
                for z in valores:
                    for w in valores:
                        mapa.append("%s%s%s%s" %(x,y,z,w))
        for x in range(len(mapa)):
            if count<=9:
                print "(%s )---%s:->%s" %(x,mapa[x],self.__base_pattern[x])
            else:
                print "(%s)---%s:->%s" %(x,mapa[x],self.__base_pattern[x])
            count+=1
        print ""
        print self.__base_pattern

    # @info: Inicializador neuronal
    def _memory_init_0(self):
        lib_nas._layer_1_1_(self.__neuron_0,self.__bias,lib_nas._memory_(self.__bias))
        lib_nas._layer_1_1_(self.__neuron_1,self.__bias,lib_nas._memory_(self.__bias))
        lib_nas._layer_1_1_(self.__neuron_2,self.__bias,lib_nas._memory_(self.__bias))

    # @info: Reseat volcados y _memory_pattern
    def _set_(self,pattern,_pattern_):
        for token in range(len(self.__base_pattern)):self.__base_pattern[token]=0
        for token in _pattern_:pattern.append(int(token))
        for token in pattern: self.__base_pattern[token]=1

#---------------------------------------------------------------------------------------- app()
# @info: app_local
def _init_net_2_(_bias_):
    n0 = _bias_4_16(_bias_)
    while True:
        try:
            _pattern=raw_input ('PATRON DESEADO: ')
            if _pattern==":q":
                break
                sys.exit(-1)
            if len(_pattern)<=16:
                n0._mapper_(_pattern)
                for x in range(16):
                    den_0_io= int(raw_input ('den_0: '))
                    den_1_io= int(raw_input ('den_1: '))
                    den_2_io= int(raw_input ('den_2: '))
                    den_3_io= int(raw_input ('den_3: '))
                    neuron_out=n0._memory_pattern_(den_0_io,den_1_io,den_2_io,den_3_io,_pattern)
                    print "------------------> %s" %neuron_out
            else:
                print "Maximo patron de aprendizaje Bias : 16 tokens"
        except:
            print "Parametro de aprendizaje incorrecto Bias:0123456789(10)(11).."

_init_net_2_(0)
