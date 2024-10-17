// 16차시 2024.10.05.토 : 프로그래머스 - 주차 요금 계산(Lv.2)
import java.util.HashMap

data class Record (
  val time: Int,
  val carNum: Int,
  val isIn: Boolean
)

class Solution {
  fun solution(fees: IntArray, records: Array<String>): IntArray {
    val sortRecords: MutableList<Record> = mutableListOf()
    
    // 주어진 기록을 파싱해서 Record 리스트로 변환
    for(record: String in records) {
      val current = record.split(" ")
      
      val timeSplit = current[0].split(":")
      val time: Int = timeSplit[0].toInt() * 60 + timeSplit[1].toInt()
      val carNum: Int = current[1].toInt()
      val isIn: Boolean = current[2] == "IN"
      
      sortRecords.add(Record(time, carNum, isIn))
    }
    
    // 입차 중인 차량들의 입차 시간을 저장하는 맵
    val inCars: HashMap<Int, Int> = HashMap()
    // 자동차 번호별 총 주차 시간을 저장하는 맵
    val parkingTimes: HashMap<Int, Int> = HashMap()
    
    // 각 레코드를 처리
    for(record: Record in sortRecords) {
      if (record.isIn) {
        // 입차 시 입차 시간을 기록
        inCars[record.carNum] = record.time
      } else {
        // 출차 시 주차 시간을 계산하고 누적
        val inTime: Int = inCars.remove(record.carNum) ?: 0
        val parkingTime = record.time - inTime
        parkingTimes[record.carNum] = parkingTimes.getOrDefault(record.carNum, 0) + parkingTime
      }
    }
    
    // 출차하지 않은 차량은 23:59에 출차된 것으로 간주
    val endTime = 23 * 60 + 59
    for((carNum, inTime) in inCars) {
      val parkingTime = endTime - inTime
      parkingTimes[carNum] = parkingTimes.getOrDefault(carNum, 0) + parkingTime
    }
    
    // 자동차 번호 순으로 결과를 계산
    val result: MutableList<Pair<Int, Int>> = mutableListOf()
    for((carNum, parkingTime) in parkingTimes) {
      var cost: Int = fees[1] // 기본 요금
      val overTime = parkingTime - fees[0]
      
      // 기본 시간을 넘은 경우 추가 요금을 계산
      if (overTime > 0) {
        cost += (overTime / fees[2]) * fees[3]
        if (overTime % fees[2] > 0) {
          cost += fees[3]
        }
      }
      
      result.add(Pair(carNum, cost))
    }
    
    // 자동차 번호 순으로 정렬 후 요금만 반환
    return result.sortedBy { it.first }.map { it.second }.toIntArray()
  }
}