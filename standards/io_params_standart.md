
# Requirements to shell scripts I/O params styles

## Common

### defines

io.type = iface.io.getType(string)

def input_source(): # input source
def output_source(): # output source

### Simetric input & output params format

;; Определение базовой структуры пути через λ-выражения
(define make-path
  (λ (dir file tmpl)
    (λ (msg)
      (case msg
        ('dir  dir)
        ('file file)
        ('tmpl tmpl)))))

;; Общий валидатор
(define validate-path
  (λ (path validator)
    (λ (error-handler)
      (if (validator path)
          path
          (error-handler path)))))

;; Специфичные валидаторы как частичное применение
(define validate-input
  (validate-path input-exists?))

(define validate-output
  (validate-path output-valid?))
  