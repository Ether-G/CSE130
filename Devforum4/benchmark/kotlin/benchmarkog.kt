fun main() {
    val iterations = 1000000
    
    repeat(iterations) {
        val grade = 95  // Test case
        var message = when(grade) {
            in 90..100             -> "Great Job!"
            in 80..89              -> "Solid work"
            in 60..79             -> "Perhaps more work is needed"
            in 1..59              -> "Please try again"
            0                      -> "Failed to submit"
            !in 101..Int.MAX_VALUE -> "Unbelievable"
            else                   -> "Invalid"
        }
    }
}