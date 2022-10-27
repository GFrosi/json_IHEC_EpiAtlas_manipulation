import pandas as pd
import sys



def merge_ihec_metadata(df_md5, df_ihec_hg19, df_ihec_hg38, out_file):

    df_merge_hg19 = df_md5.merge(df_ihec_hg19, how='left', left_on='ihec_md5sum_hg19', right_on='md5sum')
    df_merge_hg38 = df_merge_hg19.merge(df_ihec_hg38, how='left', left_on='ihec_md5sum_hg38', right_on='md5sum')

    #renaming columns
    df_merge_hg38.columns = df_merge_hg38.columns.str.replace('_x', '_hg19')
    df_merge_hg38.columns = df_merge_hg38.columns.str.replace('_y', '_hg38')  

    df_merge_hg38.to_csv(out_file, sep='\t', index=False)


def main():

    # print('frosi')
    df_md5 = pd.read_csv(sys.argv[1], sep='\t')
    df_ihec_hg19 = pd.read_csv(sys.argv[2], sep='\t')
    df_ihec_hg38 = pd.read_csv(sys.argv[3], sep='\t')
    out_file = sys.argv[4]

    merge_ihec_metadata(df_md5, df_ihec_hg19, df_ihec_hg38, out_file)



if __name__ == "__main__":

    main()