#! /usr/bin/env python3

import vcf

__author__ = 'Christian Jansen'


class Assignment2:
    
    def __init__(self, path):
        ## Check if pyvcf is installed
        if vcf.VERSION == None:
            exit("pyvcf not installed")
        self.vcf_path = path
        print("PyVCF version: %s" % vcf.VERSION)
        

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''
        quality_sum = 0
        count = 0
        for item in vcf.Reader(filename=self.vcf_path):
            quality_sum += item.QUAL
            count += 1
        quality_avg = quality_sum/count
        return quality_avg
        
        
    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''
        count = 0
        for item in vcf.Reader(filename=self.vcf_path):
            count += 1

        return count

    
    
    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return: 
        '''
        caller = set([])
        for item in vcf.Reader(filename=self.vcf_path):
            for model in item.INFO['callsetnames']:
                caller.add(model)
        return caller
        
        
    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return: 
        '''
        ref = set([])

        for item in vcf.Reader(filename=self.vcf_path):
            if 'difficultregion' in item.INFO.keys():
                for model in item.INFO['difficultregion']:
                    ref.add(model)

        return ref

    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''
        print("TODO")
        

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return: 
        '''
        print("TODO")
        
    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return: 
        '''
        print("TODO")
        
    
    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        print("TODO")
        
        print("Number of total variants")
        
    
    def print_summary(self):
        #print("DEVELOPMENT: ", self.get_human_reference_version())
        print("Average quality of the file ", self.vcf_path, ": ", self.get_average_quality_of_file())
        print("Total number of variations: ", self.get_total_number_of_variants_of_file())
        print("Variant callers used: ", self.get_variant_caller_of_vcf())
        print("Reference version: ", self.get_human_reference_version())
        print("Anmerkung: Es war mir nicht möglich die reference version hg38 im file zu finden außer in den difficult regions, daher habe ich diese hier ausgegeben.")


        print("Print all results here")
    
    
def main():
    print("Assignment 2")
    assignment2 = Assignment2("chr21_new.vcf")
    assignment2.print_summary()
    print("Done with assignment 2")
        
        
if __name__ == '__main__':
    main()
   
    



