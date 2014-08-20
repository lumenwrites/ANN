; Create a neuron
(defun make-neuron [lst])

; Create a layer
(defun make-layer [lst])

; Combine layers into netwrok
(defun make-network [inputs layers outputs])

; Train the network
(defun train-network [network examples learning-rate])

;; Define input
(setv t '(1 1 1
          0 1 0
          0 1 0))

(setv o '(1 1 1
          1 0 1
          1 1 1))

(setv i '(1 1 1
          0 1 0
          1 1 1))

(setv u '(1 0 1
          1 0 1
          1 1 1))

;;Define output(examples)

(setv letters [
               ['t [1 0 0 0]]
               ['o [1 0 0 0]]
               ['i [1 0 0 0]]
               ['u [1 0 0 0]]
               ])


; Create Network
(setv test-network (make-network '(9 8 4)); 9 inputs, 3 layers, 4 outputs
; Train the network ;; using gradient descent.
(setv trained-test-network (train-network test-network letters 
                                          (defun activation-function)
                                          
