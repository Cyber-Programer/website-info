cd ..
apt-get update -y
apt-get upgrade -y
apt-get install python -y
apt-get install git -y
rm -rf 'website-info'
git clone https://github.com/Cyber-Programer/website-info.git
cd 'website-info'
python main.py -h