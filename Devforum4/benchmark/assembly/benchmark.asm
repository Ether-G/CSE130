section .data
    iterations dd 1000000
    test_grade dd 95       ; Same test case as Kotlin
    fmt db "Assembly completed %d iterations", 10, 0

section .text
    extern printf
    global main

main:
    push ebp
    mov ebp, esp

    mov ecx, [iterations]
benchmark_loop:
    push ecx        ; Save our counter

    ; Original grade checking code
    mov eax, [test_grade]
    mov edx, 0
    mov ebx, 10
    div ebx        ; eax now contains grade/10
    
    ; Start comparisons
    cmp dword [test_grade], 100
    jg unbelievable_case    
    
    cmp eax, 9              
    jge great_job_case
    
    cmp eax, 8              
    je solid_work_case
    
    cmp eax, 6              
    jge more_work_case
    
    cmp eax, 0              
    je check_zero
    
    jmp try_again_case      

check_zero:
    cmp dword [test_grade], 0
    je failed_case
    jmp try_again_case

unbelievable_case:
great_job_case:
solid_work_case:
more_work_case:
try_again_case:
failed_case:
continue_loop:
    pop ecx         ; Restore our counter
    loop benchmark_loop

    ; Print results
    push dword [iterations]
    push fmt
    call printf
    add esp, 8

    mov esp, ebp
    pop ebp
    ret