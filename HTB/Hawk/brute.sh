#!/bin/bash

cipherlist="AES-128-CBC
AES-128-CBC-HMAC-SHA1
AES-128-CBC-HMAC-SHA256
id-aes128-CCM
id-aes128-GCM
id-aes192-CCM
id-aes192-GCM
id-aes256-CCM
id-aes256-GCM
id-aes256-wrap
id-aes256-wrap-pad
id-smime-alg-CMS3DESwrap
rc2
rc2-128
rc2-40
RC2-40-CBC
rc2-64
RC2-64-CBC
RC2-CBC
RC2-CFB
RC2-ECB
RC2-OFB
RC4
RC4-40
RC4-HMAC-MD5
seed
SEED-CBC
SEED-CFB
SEED-ECB
SEED-OFB
sm4
SM4-CBC
SM4-CFB
SM4-CTR
SM4-ECB
SM4-OFB"

digestlist="RSA-MD4
RSA-MD5
RSA-RIPEMD160
RSA-SHA1
RSA-SHA1-2
RSA-SHA224
RSA-SHA256
RSA-SHA3-224
RSA-SHA3-256
RSA-SHA3-384
RSA-SHA3-512
RSA-SHA384
RSA-SHA512
RSA-SHA512/224
RSA-SHA512/256
RSA-SM3
SHA1
sha1WithRSAEncryption
SHA224
sha224WithRSAEncryption
SHA256
sha256WithRSAEncryption
SHA3-224
SHA3-256
SHA3-384
SHA3-512
SHA384
sha384WithRSAEncryption
SHA512
SHA512-224
sha512-224WithRSAEncryption
SHA512-256
sha512-256WithRSAEncryption
sha512WithRSAEncryption
SHAKE128
SHAKE256
SM3
sm3WithRSAEncryption
ssl3-md5
ssl3-sha1
whirlpool"

encoded_file="drupal.enc"
passlist="/usr/share/wordlists/rockyou.txt"


readarray -t cipher_arr <<< $cipherlist
readarray -t digest_arr <<< $digestlist

for i in ${cipher_arr[@]};
do
	for j in ${digest_arr[@]};
	do
		echo -e "\n Trying with digest $j \n"
		#bruteforce-salted-openssl -c $i -d $j -t 40 -f $passlist $encoded_file
		bruteforce-salted-openssl -d $j -t 40 -f $passlist $encoded_file
	done

done
