import pandas as pd
import sys



def add_metadata(df_38, df_19, df_metadata,output):

    df_assembly = merge_hg38_hg19(df_38, df_19)
    # print(df_assembly.columns)
    # sys.exit()
    df_merge = df_assembly.merge(df_metadata, left_on='epiatlas_md5sum', right_on='md5sum',how='left')
    df_merge.to_csv(output, sep='\t', index=False)


def merge_hg38_hg19(df_38, df_19):

    #adding assembly columns 
    df_38['assembly_hg38'] = 'hg38'
    df_19['assembly_hg19'] = 'hg19'

    #merge
    df_hg39_hg19 = df_38.merge(df_19, on='epiatlas_md5sum', how='outer')

    #renaming columns
    df_hg39_hg19.columns = df_hg39_hg19.columns.str.replace('_x', '_hg38')
    df_hg39_hg19.columns = df_hg39_hg19.columns.str.replace('_y', '_hg19')

    return df_hg39_hg19


def main():

    df_38 = pd.read_csv(sys.argv[1], sep='\t') #tsv file hg38_md5_match_ihec_epiatlas
    df_19 = pd.read_csv(sys.argv[2], sep='\t') #tsv file hg19_md5_match_ihec_epiatlas
    metadata_file = pd.read_csv(sys.argv[3], sep='\t') #metadata file generated by json_to_csv using the complete json file (epiatlas_2020 + merged json
    output = sys.argv[4] #output file 
    add_metadata(df_38, df_19, metadata_file, output)



if __name__ == "__main__":



    main()