(import [linreg.models [Point]])
(import [numpy :as np])

;;; Hw.
(defn h-fun [w1 x w0]
  (+ (* w1 x) w0))

;;; Loss function
(defn loss-function [w1 w0 points]
  (setv loss-total 0)
  (for [point points]
    (setv loss-total
          (+ loss-total
             (np.square (-  point.posy (h-fun w1 point.posx w0))))))

  (setv loss-mean (/ loss-total
                     (len points)))
  loss-mean)


;;; Update w0
(defn w0-update [w1 w0 points]
  (setv w-change 0)
  (for [point points]
    (setv w-change
          (+ w-change
             (-  point.posy (h-fun w1 point.posx w0)))))
  w-change)

;;; Update w1
(defn w1-update [w1 w0 points]
  (setv w-change 0)
  (for [point points]
    (setv w-change
          (+ w-change
             (* (-  point.posy (h-fun w1 point.posx w0))
                point.posx))))
  w-change)



(defn regression [points]
  (setv w0-prev -10)
  (setv w1-prev -10)
  (setv w1 0)
  (setv w0 0)
  (setv learning-rate 0.1)  

  ;; Repeat until convergnece, until difference between uptades is very small
  (while (and  (> (np.square (- w0 w0-prev)) 1)
               (> (np.square (- w1 w1-prev)) 1))

    ;; Save previous weight to compare it to the new one
    (setv w0-prev w0)
    ;; Update the weight, multiplied by the learning rate
    (setv w0 (+ w0
                (*  learning-rate
                    (w0-update w1 w0 points))))

    ;; Save previous weight to compare it to the new one
    (setv w1-prev w1)
    ;; Update the weight, multiplied by the learning rate    
    (setv w1 (+ w1
                (*  learning-rate
                    (w1-update w1 w0 points))))
    (print (+ "w0 " (str w0)))
    (print (+ "w1 " (str  w1)))    
    )

  ;; Return the resulting weights
  (setv w1 0.8)
  (setv w0 1)  
  [w1 w0])
