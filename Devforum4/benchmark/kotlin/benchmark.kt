fun main() {
    val iterations = 1000000
    
    repeat(iterations) {
        val grade = 95  // Test case
        val message = when(grade/10) {
            9, 10 -> if(grade <= 100) "Great Job!" else "Unbelievable"
            8 -> "Solid work"
            6, 7 -> "Perhaps more work is needed"
            in 1..5 -> "Please try again"
            0 -> if(grade == 0) "Failed to submit" else "Please try again"
            else -> "Unbelievable"
        }
    }
}