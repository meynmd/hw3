from collections import defaultdict
import numpy as np


def read_construct_data(file_name):
    j_e_dis=defaultdict(dict)
    fp=open(file_name)
    count =0
    for line in fp.readlines():
        line1=line.split('\n')[0]
        line1=line1.split(' ')





        if count==0:
            eng_phos = np.array(line1)
            count+=1
            continue
        if count==1:
            jap_phos = np.array(line1)
            count+=1
            continue

        if count == 2:
            mapping_list = np.array([ int(temp) for temp in line1])
            #print(mapping_list)
            for i in range(len(eng_phos)):
                key = eng_phos[i]
                if key not in  j_e_dis:
                    j_e_dis[eng_phos[i]] = defaultdict(float)

                ind = i+1
                positions = np.where(mapping_list==ind)[0]
                if len(positions)>3:
                    continue

                key1=' '.join(jap_phos[positions])
                j_e_dis[key][key1]+=1

            count=0

    final_dict ={}
    for key in j_e_dis:
        total_val =sum(j_e_dis[key].values())
        if key not in final_dict:
            final_dict[key] = {}
        final_dict[key]={key1:round(j_e_dis[key][key1]/total_val,3) for key1 in j_e_dis[key]}



    return final_dict






def writing_prob(prob,output_file):
    fp=open(output_file,mode='w')
    for key in prob:
        temp_dict=sorted(prob[key],key=prob[key].get,reverse=True)
        for key1 in temp_dict:
            temp_str = key + ' : ' + key1+ ' # '+ str(prob[key][key1])+'\n'
            fp.write(temp_str)













# if __name__ == '__main__':
#     file_name = 'epron-jpron.data'
#     output_file = 'epron-jpron.probs'
#     prob=read_construct_data(file_name)
#     #writing_prob(prob,output_file)


