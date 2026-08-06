#!/bin/bash
#SBATCH --job-name=pika-ergom
#SBATCH --account=project_2012773
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=1G
#SBATCH -o stdout.log
#SBATCH -e stderr.log
#SBATCH --ntasks=1
#SBATCH --nodes=1

param="w_cya"
test_values=("0.0" "1.0" "2.0")

# loop over configurations
for i in $(seq 0 2);
do
	val=${test_values[i]}
	echo ${val}
	run="${param}_${val}"
	echo ${run}
	sed -i "s/ctrl/$run/" configure.py

	var_dec="global ${param}"
	echo $var_dec
	sed -i "s/$var_dec/tmp_tag/" cgt_init_constants.py

	value="${param}=${val}#"
	echo ${value}
	sed -i "s/$param/$value/" cgt_init_constants.py
	
	sed -i "s/tmp_tag/$var_dec/" cgt_init_constants.py

	python run.py

	# restore default values
	sed -i "s/$run/ctrl/" configure.py
	sed -i "s/$value/$param/" cgt_init_constants.py
done
