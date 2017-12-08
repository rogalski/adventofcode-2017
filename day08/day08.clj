; Some readability helpers
(defn reg [instruction] (get instruction 0))
(defn reg-op [instruction] (get instruction 1))
(defn reg-value [instruction] (read-string (get instruction 2)))

(defn cond-reg [instruction] (get instruction 4))
(defn cond-op [instruction] (get instruction 5))
(defn cond-value [instruction] (read-string (get instruction 6)))

; I/O based helpers
(defn to-instruction [line] ( clojure.string/split line #"\s+" ))
(defn get-file-lines [filename] (with-open [rdr (clojure.java.io/reader filename)] (doall (line-seq rdr))))

; Our "processor" logic
(defn make-condition [instruction] (
  case (cond-op instruction)
  "==" (fn [registers] (= (get registers (cond-reg instruction) 0) (cond-value instruction)))
  "!=" (fn [registers] (not (= (get registers (cond-reg instruction) 0) (cond-value instruction))))
  ">=" (fn [registers] (not (< (get registers (cond-reg instruction) 0) (cond-value instruction))))
  "<=" (fn [registers] (not (> (get registers (cond-reg instruction) 0) (cond-value instruction))))
  "<" (fn [registers] (< (get registers (cond-reg instruction) 0) (cond-value instruction)))
  ">" (fn [registers] (> (get registers (cond-reg instruction) 0) (cond-value instruction)))
))
(defn should-execute-instruction? [registers instruction] ( (make-condition instruction) registers))
(defn make-instruction [instruction] (
  case (reg-op instruction)
 "inc" (fn [registers] (assoc registers (reg instruction) (+ (get registers (reg instruction) 0) (reg-value instruction))))
 "dec" (fn [registers] (assoc registers (reg instruction) (- (get registers (reg instruction) 0) (reg-value instruction))))
))
(defn execute-instruction [registers instruction] ( (make-instruction instruction) registers))
(defn execute [registers instruction] (if (should-execute-instruction? registers instruction) (execute-instruction registers instruction) registers) )
(defn run-program  [filename] (reduce execute (hash-map) (map to-instruction (get-file-lines filename))))
(defn run-program-with-steps  [filename] (reductions execute (hash-map) (map to-instruction (get-file-lines filename))))

; final aggregators
(defn max-register-value [registers] (val (apply max-key val registers)))
(defn max-register-value-in-history [registers_list] (apply max (map max-register-value (remove empty? registers_list))))

(println "Advent of code 2017 Day 08!")
(println "Solution to test problem is" (max-register-value (run-program "test.txt")))
(println "Solution to problem is" (max-register-value (run-program "data.txt")))
(println "Solution 2 to test problem is" (max-register-value-in-history(run-program-with-steps "test.txt")))
(println "Solution 2 to problem is" (max-register-value-in-history(run-program-with-steps "data.txt")))
