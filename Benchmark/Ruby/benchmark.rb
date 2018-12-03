class Chrono
	 
	def initialize()
		@start = Time.now
	end
			
	def elapsed_time
		now = Time.now
		elapsed = now - @start
		elapsed.to_s
	end
	       
end

c = Chrono.new
a=0
for i in 0..10000
	for j in 0..10000
		a += 1
	end
end

puts c.elapsed_time + ' secondes'
