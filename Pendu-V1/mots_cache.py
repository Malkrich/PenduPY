#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fonction retournant le mot à afficher selon les lettres trouvées
"""

def mots_cache(mots,lettres_trouvees):
    mots_cache = ""
    
    for i in range(len(lettres_trouvees)):
        if lettres_trouvees[i] == 1:
            mots_cache+=mots[i]+" "
        elif lettres_trouvees[i] == 0:
            mots_cache+="_"+" "
    
    return mots_cache