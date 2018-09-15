import hashlib


def checkio(data,algorithm):
	return getattr(hashlib,algorithm)(data.encode()).hexdigest()

print(checkio('welcome', 'md5')) # '40be4e59b9a2a2b5dffb918c0e86bhe3d7'