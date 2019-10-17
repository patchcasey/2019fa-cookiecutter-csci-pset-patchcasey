if __name__ == "__main__":

	if '{{cookiecutter.install_csci_utils}}' == 'no':
		with open('Pipfile', "r") as f:
			lines = f.readlines()
		#below list comprehension adapted from: https://stackoverflow.com/questions/19286657/index-all-except-one-item-in-python
		lines_to_write = [x for i,x in enumerate(lines) if i!=10]
		with open('Pipfile','w') as f:
			for line in lines_to_write:
				f.write(line)
