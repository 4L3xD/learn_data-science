dictionary = {
            "Computação":
               {
                   "Ciência de Dados":
                   {
                       "Inteligência Artificial":
                       {
                           "Machine Learning":
                           {
                               "Deep Learning":
                               {
                                   "Image Recognition": ["Face Recognition", "Object Recognition", "..."],
                                   "Natural Language Processing (NLP)":
                                   {
                                       "Voice Recognition": "...",
                                       "Text processing": ["Translator", "..."],
                                       "Emotion analysis": "..."
                                   }
                               }
                           }
        
                       }
                   }
               },
            "Ciências Sociais": ["Filosofia", "Sociologia", "Antropologia", "Economia", "Ciência Política", "História", "Geografia", "Educação"]
        }      

#print(dict.values()) #dict_values([{'Ciência de Dados': {'Inteligência Artificial': {'Machine Learning': {'Deep Learning': {'Image Recognition': ['Face Recognition', 'Object Recognition', '...'], 'Natural Language Processing (NLP)': {'Voice Recognition': '...', 'Text processing': ['Translator', '...'], 'Emotion analysis': '...'}}}}}}, ['Filosofia', 'Sociologia', 'Antropologia', 'Economia', 'Ciência Política', 'História', 'Geografia', 'Educação']])
#print(dict.keys()) #dict_keys(['Computação', 'Ciências Sociais'])

#for current in dictionary:
#   print (dictionary.get(current))

for key, value in dictionary.items():
    #print (key, value)
    if isinstance(value, list):
        #print(value)
        for item in value:
            print(f"List: {key} - {item}")
    if isinstance(value, dict):
        #print(value)
        for sub_key, sub_value in value.items():
            #print(f"Dict: {key} - {sub_value}")
            if isinstance(sub_value, dict):
                for sub_key_ii, sub_value_ii in sub_value.items():
                    if isinstance(sub_value_ii, dict):
                        for sub_key_iii, sub_value_iii in sub_value_ii.items():
                            #print(f"{key} - {sub_key} - {sub_key_ii} - {sub_key_iii}")
                            if isinstance(sub_value_ii, dict):
                                for sub_key_iv, sub_value_iv in sub_value_iii.items():
                                    #print(f"{key} - {sub_key} - {sub_key_ii} - {sub_key_iii} - {sub_key_iv}")
                                    if isinstance(sub_value_iv, dict):
                                        for sub_key_v, sub_value_v in sub_value_iv.items():
                                            #print(f"{key} - {sub_key} - {sub_key_ii} - {sub_key_iii} - {sub_key_iv} - {sub_key_v}")
                                            if isinstance(sub_value_v, dict):
                                                for sub_key_vi, sub_value_vi in sub_value_v.items():
                                                    print(f"* {key} - {sub_key} - {sub_key_ii} - {sub_key_iii} - {sub_key_iv} - {sub_key_v} - {sub_key_vi}")
                                                    if isinstance(sub_value_vi, list):
                                                        print(f"   - {sub_value_vi}")
                                                    else: print(f"* {sub_value_vi}")
                                            else:
                                                print(f"* {key} - {sub_key} - {sub_key_ii} - {sub_key_iii} - {sub_key_iv} - {sub_key_v}:")
                                                for item in dictionary[key][sub_key][sub_key_ii][sub_key_iii][sub_key_iv][sub_key_v]:
                                                    print(f"   - {item}")
                            




#for tag in dictionary.keys():
#    print(f"Grande área: {tag}")
#    for subt in dictionary[tag]:
#        print(subt)
#        for isubt in dictionary[tag][subt]:
#            #print(isubt)
#            for iisubt in dictionary[tag][subt][isubt]:
#                #print(iisubt)
#                for iiisubt in dictionary[tag][subt][isubt][iisubt]:
#                    #print(iiisubt)
#                    for visubt in dictionary[tag][subt][isubt][iisubt][iiisubt]:
#                        #print(visubt)
#                        for vsubt in dictionary[tag][subt][isubt][iisubt][iiisubt][visubt]:
#                            print(vsubt)
#                            try:
#                                for visubt in dictionary[tag][subt][isubt][iisubt][iiisubt][visubt][vsubt]:
#                                    print(visubt)
#                            except:
#                                print()