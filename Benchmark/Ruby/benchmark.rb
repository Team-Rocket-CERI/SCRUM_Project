class Chrono
	 
	  def initialize()
		      @start = Time.now
		        end
	     
	    def elapsed_time
		        now = Time.now
			    elapsed = now - @start
			        puts 'Started: ' + @start.to_s
				    puts 'Now: ' + now.to_s
				        puts 'Elapsed time: ' +  elapsed.to_s + ' seconds'
					    elapsed.to_s
					      end
	       
end

## Usage

c = Chrono.new
a=0
for i in 0..10000
	for j in 0..10000
			a += 1
				end
				end
				puts c.elapsed_time
