
import requests
import time

# return 0 = crashing ; 1 = activity
def check_server_status():
	#crashing logs 
	crashing_log = "Your app is crashing. Here's the latest log"
	#r = requests.get('https://api.github.com/events')

	target_url = "http://140.116.37.28:3000/dashboard4"
	#r = requests.get(target_url, auth=('user', 'pass'))
	try:
		r = requests.get(target_url)
		if r.status_code != 200:
			print ('server[%d] is death at %s.')%(r.status_code,time.ctime())
			return (2,'death[%d]'%r.status_code)
		#print r.status_code

		if crashing_log in r.text :
			print ('server is crashing at %s.')%time.ctime()
			return (0,'crashing')
		else:
			print ('server is activity at %s.')%time.ctime()
			return (1,'activity')
	except:
		print ('server is error at %s.')%time.ctime()
		return (4,'error')
	
def write_log(status_message):
	message = ("%s : %s\r\n") % (status_message,time.ctime())

	with open("server_logs.txt", "a") as file:
		file.write(message)
		#file.write('\r\n')
	pass
def main():
	print 'start ...'
	temp_server_status_code = -1

	while(True):
		current_status_code,current_status = check_server_status()
		if temp_server_status_code != current_status_code:
			write_log(current_status)
			temp_server_status_code = current_status_code
		time.sleep(60)

if __name__ == '__main__':
	main()

