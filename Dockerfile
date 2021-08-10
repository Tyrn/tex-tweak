FROM python:3.9-slim

ARG user=procr project=tex-tweak src=tex_tweak

# Non-root user.
RUN useradd -ms /bin/bash "$user"
USER $user
WORKDIR /home/$user
ENV PATH=/home/$user/.local/bin:$PATH

# Source and project files.
RUN mkdir /home/$user/$project
WORKDIR /home/$user/$project
COPY $src ./$src/
COPY pyproject.toml .
#COPY poetry.lock .

# Build.
RUN pip install poetry --user
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry build
RUN ttk .

#CMD [ "python", "./server.py" ]
CMD echo "Hello, World!"