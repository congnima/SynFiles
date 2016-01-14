import filecmp
import os.path


def find_difference(src_dir, des_dir):
    """
    find difference between src_dir and des_dir, which files and directoies are only in src_dir
    or the files and sub-directoies which has the same name but different contents or modified time

    @param src_dir : source directory
    @param des_dir : destination directory
    @return: a list of files or directories that are different
    """
    dcmp = filecmp.dircmp(src_dir,des_dir)
    dcmp.report_full_closure()

    print '\n'

    lst = list()

    #files only in source directory or destination directory
    lst += dcmp.left_only


    #files different
    for f in dcmp.diff_files:
        lst.append(f)

    #print lst

    #files different in common subdirectory
    for f in dcmp.common_dirs:
        lst_subdir = list()
        lst_subdir = find_difference(os.path.join(src_dir,f),
                            os.path.join(des_dir,f))
         
        lst_subdir = [ os.path.join(f,fn) for fn in lst_subdir ]
        lst += lst_subdir
               
    return lst



def do_copy(src_dir, des_dir,lst):
    """
    copy files or subdirectoies from src_dir to des_dir 

    @param src_dir:
    @param des_dir: 
    @param lst : type list, stores the files' path get from function find_diffenrence
    """
    for f in lst:
        import distutils.file_util
        import distutils.dir_util
        print "from %s copy to %s ..." % (os.path.join(src_dir,f), os.path.join(des_dir,f))
        if os.path.isdir(os.path.join(src_dir,f)):
            distutils.dir_util.mkpath(os.path.join(des_dir,f))
            distutils.dir_util.copy_tree(os.path.join(src_dir,f),os.path.join(des_dir,f))
        else:
            distutils.file_util.copy_file(os.path.join(src_dir,f),os.path.join(des_dir,f))