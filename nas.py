
#Modulo class_neurona
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os.path
from goto import with_goto

#nas.py 
# Neuron artificial binaria dimensional 
# @autor:Jose Luis Prado Seoane ---IT Security Researcher & Developer
#
# Research: Teoria de Sistemas Neuronales (I.A) --TSNB
# Redes Neuronales y su convergencia hacia modelos e implementaciones orientadas a la
# Ciberseguridad

# Descripcion: ***********************************************************************
# Neurona artificial de tipo binaria con salida en escalon en el segmento [0,1] que determina 
# dos areas o patrones de deteccion para resolucion de problemas linealmente separables.
# La misma es recursiva y con aprendizaje en pesos en los Imputs, donde reside el aprendizaje 
# de la misma. Establece diferentes estados logicos auto-programables lo que la convierte en 
# logica dinamica adaptable que permitira como se vera mas adelante introducir mejoras en lo 
# que a patrones y adaptabilidad se refiere a traves de una clase que la determina.
#
#Pragma: Actualmente se han incorporado al Research: @n4ivenom
# Se necesita instalar el modulo < goto > externo para la recursividad
# @info
# @class: Clase --neuronal artificial

class neuron(object):
    # @info
    # @def:__Constructor__
    def __init__(self,id_):
        self.__learning = 0.5
        self.__id_ = int(id_)
        self.__ref_class = self.__class__.__name__ + "_" + str(self.__id_)
        self.__memory_ = "rnl_sinap_ia_" + self.__ref_class

    # @info
    # @def:__inputs__
    def ibn_(self,den_0_io=0,den_1_io=0,axon_ptron=11):
        self.__dendrite_0_io = int(den_0_io)
        self.__dendrite_1_io = int(den_1_io)
        self.__axon_ptron_out = int(axon_ptron)
        self._out_ = 0

        if self.__axon_ptron_out != 11:
            self.sinap()
        else:
            self._memory_back_sinap(self.__dendrite_0_io,self.__dendrite_1_io)

    # @info
    # @def:Reseat __memory__
    def rst_sign_(self):
        if os.path.exists(self.__memory_) != 0:
            os.remove(self.__memory_)

    # @info
    # @def:__sinaptica__
    @with_goto
    def sinap(self):
        pesos=[];_mem_=[]
        for x in range(2):
            pesos.append(random.uniform(0,1))
        entradas=[self.__dendrite_0_io,self.__dendrite_1_io]
        salida=0;corrector=0
        label.backend
        sumatoria = self.funcionActivacion(entradas,pesos)

        if sumatoria > 0:salida=1;corrector = -2.0
        elif sumatoria<=0:salida=0;corrector = 2.0

        if cmp(salida,self.__axon_ptron_out)!=0:
            for i,x in enumerate(pesos):
                if self.__axon_ptron_out == 0:
                    pesos[i]=pesos[i] + (corrector * self.__learning)
                elif self.__axon_ptron_out == 1:
                    salida = 1
                    goto.frontend
            goto.backend
        else:
            label.frontend
            rnl_map_sinap = open(self.__memory_,"a+")
            _bin_ = str(bin(self.__dendrite_0_io) + bin(self.__dendrite_1_io))
            _mem_.append(self.__ref_class);_mem_.append(_bin_[2] + _bin_[5])
            _mem_.append(pesos[0]);_mem_.append(pesos[1]);_mem_.append(sumatoria)
            rnl_map_sinap.write(str(_mem_) + '\n')
            rnl_map_sinap.close()
    
    # @info
    # @def:__back_with_learning
    @with_goto
    def _memory_back_sinap(self,den_0_io,den_1_io):
        adrr_memory = [];pesos=[];_offset_= 1
        _bin_ = str(bin(self.__dendrite_0_io) + bin(self.__dendrite_1_io))
        _mem_ = (_bin_[2] + _bin_[5])
        rnl_map_sinap = open(self.__memory_,"r")
        v_offset_ = str(self.__id_);_offset_ = len(v_offset_)

        for w_ibn in rnl_map_sinap.readlines():
            if (_mem_ == '00' and w_ibn[14 + (_offset_- 1):16 + (_offset_- 1)] == '00'):
                adrr_memory.append(w_ibn.split(',')[2]);adrr_memory.append(w_ibn.split(',')[3]);break
            elif (_mem_ == '01' and w_ibn[14 + (_offset_- 1):16 + (_offset_- 1)] == '01'):
                adrr_memory.append(w_ibn.split(',')[2]);adrr_memory.append(w_ibn.split(',')[3]);break
            elif (_mem_ == '10' and w_ibn[14 + (_offset_- 1):16 + (_offset_- 1)] == '10'):
                adrr_memory.append(w_ibn.split(',')[2]);adrr_memory.append(w_ibn.split(',')[3]);break
            elif (_mem_ == '11' and w_ibn[14 + (_offset_- 1):16 + (_offset_- 1)] == '11'):
                adrr_memory.append(w_ibn.split(',')[2]);adrr_memory.append(w_ibn.split(',')[3]);break
        rnl_map_sinap.close()
        entradas=[self.__dendrite_0_io,self.__dendrite_1_io]

        for w_ret in adrr_memory:
            pesos.append(float(w_ret))
        sumatoria = self.funcionActivacion(entradas,pesos)
        #self._out_ = sumatoria
        if sumatoria > 0:self._out_=1#;corrector = -10.0
        elif sumatoria<=0:self._out_=0#;corrector = 10.0

    # @info
    # @def:__func_activacion__lineal_separable__
    def funcionActivacion(self,entradas,pesos):
        sumatoria=0
        for i,entrada in enumerate(entradas):
            sumatoria = sumatoria + (entradas[i]*pesos[i])
        if sumatoria == 0.0:
            for i,entrada in enumerate(entradas):
                sumatoria = sumatoria + (1 * pesos[i])
                return sumatoria
        else:
            return sumatoria
