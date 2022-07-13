import string
import numpy as np

def scheme():
    letters = list(string.ascii_lowercase)
    values = [i for i in range(0,26)]
    scheme = dict(zip(letters,values))
    return scheme

def get_value_from_scheme(letter,sc):
    return  sc.get(letter)


def transform_on_num(plain_text,sc):
    plain_text = list(plain_text)
    text_num = []
    for letter in plain_text:
        text_num.append(get_value_from_scheme(letter,sc))
    p = np.array(text_num)

    return p
def transform_on_letter(num,sc):
    for key,value in sc.items():
        if value==num:return key

def encrypt(plain_text,key,sc):
    key_list = []
    text_num = transform_on_num(plain_text,sc)
    c = np.matmul(text_num,key)%26

    for num in c:
       key_list.append(transform_on_letter(num,sc)) 
   
    return ''.join(key_list)

#the function check_common_divisor  has been removed in :https://www.codespeedy.com/find-common-divisors-of-two-numbers-using-python/
def  check_common_divisor(a,b):
    k=0
    for i in range(1,min(a,b)+1):
          if a%i == b%i == 0:
             
             k+=1
             
    return False if k>1 else True

def generate_key(m):
    while(True):
        key = np.random.randint(26,size=(m,m))
        det  = round(np.linalg.det(key))%26
        if(det!=0 and check_common_divisor(int(det),26)):return key

def multiplicative_inverse_of_the_determinant(det):
    for num in range(1,26):
        if ((num*det)%26==1):return num
            
            
def inverse(key):

    det = round(np.linalg.det(key))%26
    m = multiplicative_inverse_of_the_determinant(det)
    
    matrix_cofactor = np.linalg.inv(key).T * np.linalg.det(key)
    adj_key = matrix_cofactor.transpose()
    adj_key =np.round(adj_key)
    k_inverse = np.multiply(adj_key,m)%26

    return k_inverse   

def decrypt(decrypt_text,key,sc):
    key_inverse = inverse(key)

    decrypt_text = encrypt(decrypt_text,key_inverse,sc)
 
    return decrypt_text


def main():
    sc= scheme()
    plain_text = 'name'
    m = len(plain_text)
   
    key = generate_key(m)
    encrypt_text = encrypt(plain_text,key,sc)
    decrypt_text = decrypt(encrypt_text,key,sc)

    print('Encrypt :' + encrypt_text)
    print('Decrypt :' + decrypt_text)

  
        
    
main()