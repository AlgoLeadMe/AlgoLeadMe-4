// 11차시 2024.09.04.수 : 백준 - 축구(1344)
import java.io.BufferedReader
import java.io.InputStreamReader
import kotlin.math.pow

fun combination(n: Int, r: Int): Double {
  var result = 1.0
  for (i in 0 until r) {
    result *= (n - i).toDouble()
    result /= (i + 1).toDouble()
  }
  return result
}

fun probability(p: Double, k: Int): Double {
  return combination(18, k) * p.pow(k) * (1 - p).pow(18 - k)
}

fun main() {
  // ✅ Input
  val br = BufferedReader(InputStreamReader(System.`in`))

  var A: Double = br.readLine().toDouble() / 100.0
  var B: Double = br.readLine().toDouble() / 100.0

  val primeNumbers = setOf(2, 3, 5, 7, 11, 13, 17)
  var nonPrimeA = 0.0
  var nonPrimeB = 0.0
  for (i in 0..18) {
    if (i !in primeNumbers) {
      nonPrimeA += probability(A, i)
      nonPrimeB += probability(B, i)
    }
  }

  print(1 - (nonPrimeA * nonPrimeB))
}