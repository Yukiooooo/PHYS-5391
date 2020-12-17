subroutine print_matrix(array, n, m)
!*********************************************
! used for print array in flexible dimension
!*********************************************

  ! always start with this 
  implicit none

  ! declare variables
  real, intent(in) :: array(n,m) ! array
  integer, intent(in) :: n,m ! dimension 
  integer :: i
  
  do i = 1,n ! loops with i

     print*, array(i,:) ! print array
     print*, '******************************'
  
  end do ! end loops
end subroutine print_matrix
