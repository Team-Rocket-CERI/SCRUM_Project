start_time="$(date -u +%s)"
count=0
for i in {0..1000}
do
	for j in {0..1000}
		do
			count=$((count + 1))
		done
done

end_time="$(date -u +%s)"

elapsed="$(($end_time-$start_time))"
echo "$elapsed secondes"
