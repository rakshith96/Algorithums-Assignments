import random

def k_means(data, k):
	# 1. k initial "means" are randomly selected from the data set.
	means = random.sample(data, k)
	def kmeans1(data, means):
		# 2. k clusters are created by associating every observation with the nearest mean.
		clusters = [ [] for _ in means ]
		for d in data:
			distances = [ (abs(d-m), i) for i,m in enumerate(means) ]
			_,closest = min(distances)
			clusters[closest].append(d)
		return sorted(clusters)
	prev = []
	curr = kmeans1(data, means)
	while curr != prev:
		prev = curr
		# 3. The centroid of each of the k clusters becomes the new means.
		means = [ sum(c) / max(1,len(c)) for c in curr ]
		curr = kmeans1(data, means)
	# 4. ...repeated until convergence has been reached.
	return zip(means, curr)

if __name__ == '__main__':
	Ages = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
	print(list(k_means(Ages, 10)))

