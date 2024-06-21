func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	// have a window of size minutes, slide the window across, keep track of actual sum and window sum
	// have the window where the difference is the maximum between window sum and actual sum
	n := len(customers)
	if minutes >= n {
		// edge case
		sum := 0
		for i := 0; i < n; i++ {
			sum += customers[i]
		}
		return sum
	}

	windowSum := 0
	actualSum := 0
	totalSum := 0
	start := 0
	end := minutes - 1
	for i := 0; i <= end; i++ {
		windowSum += customers[i]
		if grumpy[i] == 0 {
			totalSum += customers[i]
			actualSum += customers[i]
		}
	}

	maxDiff := windowSum - actualSum

	start++
	end++
	for end < n {
		// windowSum stores the sat customers if no grumpiness
		windowSum += customers[end]
		windowSum -= customers[start-1]
		// for calculating the total customers satisfied
		if grumpy[end] == 0 {
			totalSum += customers[end]
			actualSum += customers[end]
		}
		if grumpy[start-1] == 0 {
			actualSum -= customers[start-1]
		}
		maxDiff = max(maxDiff, windowSum-actualSum)
		end++
		start++
	}
	return totalSum + maxDiff
}