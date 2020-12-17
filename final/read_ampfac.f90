! ******************************************************************************
! The input interface of AMPERE FAC DATA files, adapted from .txt format
! from python .nc. in mlt*mlat.  Added to this MODEL, hongyu, 12/10/2020
! ****************************************************************************** 
program read_ampfac
  ! This is the main program of our interface, call the subroutine 
  ! 'read_amp_fac' to read python output .txt; use 'print_matrix'
  ! to quickly check our results of the matrix

  ! always start with this
  implicit none

  ! declare variables we needed
  real, dimension(25,90) :: fac_obs ! input FAC matrix
  ! GITM grids: mlt * mlat
  integer               :: nmlt, nmlat
  nmlt = 25
  nmlat = 90
  
  call read_amp_fac(fac_obs) ! call funct to readin FAC
  print*, "================= quick look at FAC readin ================="
  call print_matrix(fac_obs,3,3) ! call funct to print FAC
  
end program read_ampfac ! end the main program

! *****************************************************************
subroutine read_amp_fac(fac)
  ! This subroutine is used for reading FAC file from python
  ! always start with this
  implicit none
  
  ! declare variables we needed
  real, dimension(25,90) :: fac ! AMPERE FAC obs

  integer                :: ierror ! check if open correctly
  integer, parameter     :: unit_=55 ! give an arbitrary unit_
  integer                :: m, n, i ! m for lines
  ! One line of input
  character (len=100)  :: line, filename
  ! -----------------------------------------------
  filename = "fac_2013031710_2d.txt" ! this is the python output txt
  open(unit=unit_, file=filename, iostat = ierror) ! open the txt
  if (ierror.ne.0) stop "Error opening FAC file" ! if error

  m = 0 ! accounting lines
  do ! start loop
     ! read in values & lines ==> m
     read(unit_,'(a)', iostat = ierror) line
     if (ierror.ne.0) exit ! if error, exit
    ! print*, ">> read lines <<"
     m = m + 1 ! line = line + 1
     
     ! finish the header when meet '#start'
     if(index(line,'#START')>0) then  ! stop accounting
        print*, "File header contains", m, "lines"
        
        ! read FAC into a same dimensional matrix
        read(unit_,*) fac
     endif ! end the if loop

  enddo ! end loop
  close(unit_) ! close the txt file

end subroutine read_amp_fac ! end our subroutine




