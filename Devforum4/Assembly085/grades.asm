section .data
    prompt db "Enter grade (0-100): ", 0
    prompt_len equ $ - prompt
    
    great_job db "Great Job!", 10, 0
    solid_work db "Solid work", 10, 0
    more_work db "Perhaps more work is needed", 10, 0
    try_again db "Please try again", 10, 0
    failed db "Failed to submit", 10, 0
    unbelievable db "Unbelievable", 10, 0
    
    format_in db "%d", 0
    
section .bss
    grade resb 4

section .text
    extern printf
    extern scanf
    global main

main:
    push ebp
    mov ebp, esp
    
    ; Print prompt
    push dword prompt
    call printf
    add esp, 4
    
    ; Get grade input
    push grade
    push format_in
    call scanf
    add esp, 8
    
    ; Get grade/10 for range check
    mov eax, [grade]
    mov edx, 0
    mov ebx, 10
    div ebx        ; eax now contains grade/10
    
    ; Start comparisons
    cmp dword [grade], 100
    jg unbelievable_case    ; grade > 100
    
    cmp eax, 9              ; grade/10 >= 9
    jge great_job_case
    
    cmp eax, 8              ; grade/10 = 8
    je solid_work_case
    
    cmp eax, 6              ; grade/10 >= 6
    jge more_work_case
    
    cmp eax, 0              ; grade = 0
    je check_zero
    
    jmp try_again_case      ; default for 1-59

check_zero:
    cmp dword [grade], 0
    je failed_case
    jmp try_again_case

unbelievable_case:
    push unbelievable
    jmp print_and_exit

great_job_case:
    push great_job
    jmp print_and_exit

solid_work_case:
    push solid_work
    jmp print_and_exit

more_work_case:
    push more_work
    jmp print_and_exit

try_again_case:
    push try_again
    jmp print_and_exit

failed_case:
    push failed

print_and_exit:
    call printf
    add esp, 4
    
    mov esp, ebp
    pop ebp
    ret