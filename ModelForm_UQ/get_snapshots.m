function get_snapshots(file, root)
    % Clear command is moved to only clear specific unnecessary variables if needed
    clc;
    
    addpath('/data1/yq87/CRISPS/ModelForm_UQ_ML_Potentials/toolbox/');

    % Ensure that the input arguments are correctly interpreted as char (string)
    if nargin < 2
        error('Usage: get_snapshots(file, root)');
    end

    % data_folder = char(data_folder);
    file = char(file);
    root = char(root);

    % Assemble the full root path
    root = fullfile(root);

    % Parameters
    num_ss = 7501; 
    num_atom = 1016; 
    num_states = 7; 
    headlines = 9; 

    % Output messages to console
    disp(['Reading from file: ', fullfile(root, file), ' ...']);
    disp(['Data with num_ss = ', num2str(num_ss), ' ...']);
    
    % Start timing the operation
    tic

    % Read snapshots
    ss = read_snapshots(fullfile(root, file), num_ss, num_atom, num_states, headlines);
    
    % Process snapshots
    init_qmin = reshape(ss(:,2:4, :), [num_atom*3, num_ss]);
    init_qmin = init_qmin(:,1);
    ss_q = reshape(ss(:,2:4, :), [num_atom*3, num_ss]);
    ss_q_dis = ss_q - init_qmin;
    ss_v = reshape(ss(:,5:7, :), [num_atom*3, num_ss]);

    % Save results
    save(fullfile(root, 'ss_q.mat'), 'ss_q', 'ss_q_dis', 'init_qmin');
    save(fullfile(root, 'ss_v.mat'), 'ss_v');

    % Display elapsed time
    elapsedTime = toc;
    disp(['Time elapsed: ', num2str(elapsedTime), 's']);
end
