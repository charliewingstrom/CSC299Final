import urllib.parse
import urllib.request
import json
import pylast
from crawler_abst_api import CrawlerAbstractAPI


class MyAPI (CrawlerAbstractAPI):
    """
    Encapsulates the interactions for the API used in lab.
    There are people and tags. artist is bipartite 0. Tags bipartite 1.

    Variables
    """
    
#    API_KEY="05e06f8849fea2cee2c0c55f88f4479d"
#    API_SECRET="d53664975702a7348c95f3e588f46ed7"
#    username = "meruryman"
#    password_hash = pylast.md5("Bellsprout299!")

    API_KEY="f6b5317d9f966c37f7c21bdd554094a1"
    API_SECRET="bbcced560aede1de9fafe65fd10a340b"
    username = "CS299_Bells"
    password_hash = pylast.md5("CS299!")
    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET, username=username, password_hash=password_hash)

    


    
    def initial_nodes(self):
#        initial_tag1 = '60s'
#        initial_artist1 = 'The Velvet Underground'
#        initial_artist2 = 'King Crimson'
#        initial_artist3 = 'The Beach Boys'
#        initial_artist4 = 'The Beatles'
#        initial_artist5 = 'John Coltrane'
#        initial_artist6 = 'The Doors'
#        initial_artist7 = 'Bob Dylan'
#        initial_artist8 = 'Mingus'
#        initial_artist9 = 'The Jimi Hendrix Experience'
#        initial_artist10 = 'Miles Davis'
#        initial_artist11 = 'Led Zeppelin'
#        initial_artist12 = 'Leonard Cohen'
#        initial_artist13 = 'Frank Zappa'
#        initial_artist14 = 'Love'
#        initial_artist15 = 'Pink Floyd'
#        initial_artist16 = 'The Zombies'
#        initial_artist17 = 'Nick Drake'
#        initial_artist18 = 'The Rolling Stones'
#        initial_artist19 = 'Neil Young with Crazy Horse'
#        initial_artist20 = 'Van Morrison'
#        initial_artist21 = 'The Kinks'
#        initial_artist22 = 'The Ronettes'
#        initial_artist23 = 'Pharoah Sanders'
#        initial_artist24 = 'Otis Redding'
#        initial_artist25 = 'Eric Dolphy'
        
#        init_60s = []
#        init_60s.append((initial_tag1, self.make_node_tag(initial_tag1, 0)))
        
#        init_60s_artists = self.returnTopArtistsByTag(initial_tag1, 40)
#        for artist in init_60s_artists:
#            init_60s.append((artist, self.make_node_artist(artist, 0)))

        initial_tag2 = '70s'
        init_70s = []
        init_70s.append((initial_tag2, self.make_node_tag(initial_tag2, 0)))
        
        init_70s_artists = self.returnTopArtistsByTag(initial_tag2, 40)
        for artist in init_70s_artists:
            init_70s.append((artist, self.make_node_artist(artist, 0)))
        
#        init_60s.append((initial_artist1, self.make_node_artist(initial_artist1, 0)))
#        init_60s.append((initial_artist2, self.make_node_artist(initial_artist2, 0)))
#        init_60s.append((initial_artist3, self.make_node_artist(initial_artist3, 0)))
#        init_60s.append((initial_artist4, self.make_node_artist(initial_artist4, 0)))
#        init_60s.append((initial_artist5, self.make_node_artist(initial_artist5, 0)))        
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist6, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist7, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist8, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist9, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist10, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist11, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist12, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist13, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist14, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist15, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist16, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist17, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist18, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist19, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist20, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist21, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist22, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist23, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist24, 0)))
#        init_60s.append((initial_artist6, self.make_node_artist(initial_artist25, 0)))
        
        
        
#        initial_tag2 = '70s'
#        initial_artist26 = 'Pink Floyd'
#        initial_artist27 = 'Led Zeppelin'
#        initial_artist28 = 'David Bowie'
#        initial_artist29 = 'Black Sabbath'
#        initial_artist30 = 'Joy Division'
#        initial_artist31 = 'Nick Drake'
#        initial_artist32 = 'Television'
#        initial_artist33 = 'King Crimson'
#        initial_artist34 = 'The Clash'
#        initial_artist35 = 'Bob Dylan'
#        initial_artist36 = 'Miles Davis'
#        initial_artist37 = 'Can'
#        initial_artist38 = 'Yes'
#        initial_artist39 = 'Neil Young'
#        initial_artist40 = 'The Beatles'
#        initial_artist41 = 'The Stooges'
#        initial_artist42 = 'The Rolling Stones'
#        initial_artist43 = 'The Who'
#        initial_artist44 = 'Eno'
#        initial_artist45 = 'Stevie Wonder'
#        initial_artist46 = 'Creedence Clearwater Revival'
#        initial_artist47 = 'Genesis'
#        initial_artist48 = 'Television'
#        initial_artist49 = 'Iggy and The Stooges'
#        initial_artist50 = 'Talking Heads'

#        init_70s = []
#        init_70s.append((initial_tag2, self.make_node_tag(initial_tag2, 0)))
#        init_70s.append((initial_artist7, self.make_node_artist(initial_artist21, 0)))
#        init_70s.append((initial_artist8, self.make_node_artist(initial_artist22, 0)))
#        init_70s.append((initial_artist9, self.make_node_artist(initial_artist23, 0)))
#        init_70s.append((initial_artist10, self.make_node_artist(initial_artist24, 0)))
#        init_70s.append((initial_artist11, self.make_node_artist(initial_artist25, 0)))
#        init_70s.append((initial_artist12, self.make_node_artist(initial_artist26, 0)))
      
        # return either init_60s or init_70s depending on which graph
        print("init_70s")
        print(init_70s)
        print("top artists")
        print(init_70s_artists)
#        return init_60s
        return init_70s

    def returnTopArtistsByTag(self, tagName, lim):
        tag = self.network.get_tag(tagName)
        artists = []
        artistDump = tag.get_top_artists(limit=lim)
        iterVar = 0
        while (iterVar < len(artistDump)):
            artists.append(str(artistDump[iterVar][0]))
            iterVar = iterVar + 1
        return artists

    def returnTopTagsByArtist(self, artistName, lim):
        artist = self.network.get_artist(artistName)
        tags = []
        tagDump = artist.get_top_tags(limit=lim)
        iterVar = 0
        while (iterVar < len(tagDump)):
            tags.append(str(tagDump[iterVar][0]))
            iterVar = iterVar + 1
        return tags

    def retTopTagsWeight_Artist(self, artistName, lim):
        artist = self.network.get_artist(artistName)
        data = []
        tagDump = artist.get_top_tags(limit=lim)
        iterVar = 0
        while (iterVar < len(tagDump)):
            data.append((str(tagDump[iterVar][0]), str(tagDump[iterVar][1])))
            iterVar = iterVar + 1
        return data


#    def returnTopTracksByArtist(network, artistName, lim):
#        artist = network.get_artist(artistName)
#        tracks = []
#        trackDump = artist.get_top_tracks(limit = lim)
#        iterVar = 0
#        while (iterVar < lim):
#            tracks.append(str(trackDump[iterVar][0]))
#            iterVar = iterVar + 1
#        return tracks

    def make_node_artist(self, artist, depth):
        """
        Makes a node representing an artist

        Arguments
        id -- the node id (converted to a string)
        artist -- artist's name
        depth -- depth of the search to this point
        graph -- Graph object to add the node to
        """
        nid = self.make_node(0, artist, depth)
        
        #Get playcount for artist
        art = self.network.get_artist(artist)
        playcount = art.get_playcount()
        
        #Add playcount to graph
        self._graph.nodes[nid]['playcount'] = playcount
        return nid

    def make_node_tag(self, tag, depth):
        """
        Makes a node representing a tag

        Arguments
        id -- the node id (converted to a string)
        tag -- the tag string
        depth -- depth of the search to this point
        graph -- Graph object to add the node to
        """
        nid = super().make_node(1, tag, depth)
        return nid

    def execute_artist_query(self, tag):
        """
        Executes the names query and parses the results.

        Arguments
        tag -- a tag

        Returns
        (success flag, data) -- tuple
        success flag -- true if the values were successfully parsed (no errors)
        data -- a list of names that resulted from the query
        """
        try:
            data = self.returnTopArtistsByTag(tag, 10)
            return (True, data)
        except ValueError as e:
            # Usually this means that the API call has failed
            print(e)
            return self._ERROR_RESULT
        except TypeError as e:
            print(e)
            return self._ERROR_RESULT

    def execute_tags_query(self, artist):
        """
        Executes the tags query and parses the results.

        Arguments
        name -- an artist's name

        Returns
        (success flag, data) -- tuple
        success flag -- true if the values were successfully parsed (no errors)
        data -- a list of tags that resulted from the query
        """
        try:
            data = self.returnTopTagsByArtist(artist, 10)
            return (True, data)
        except ValueError as e:
            # Usually this means that the API call has failed
            print(e)
            return self._ERROR_RESULT
        except TypeError as e:
            print(e)
            return self._ERROR_RESULT

    # These are ARTISTS bipartite 0
    def get_child0(self, node, graph, state):
        artist = graph.node[node]['label']
        success, data = self.execute_tags_query(artist)

        if success:
            # Distinguish nodes previously seen from new nodes
            old_tags = [tag for tag in data if state.is_visited(1, tag)]
            new_tags = [tag for tag in data if not (state.is_visited(1, tag))]

            # Get the existing nodes
            old_nodes = [state.visited_node(1, tag) for tag in old_tags]

            # Create the new nodes
            new_depth = graph.node[node]['_depth'] + 1
            new_nodes = [self.make_node_tag(tag, new_depth)
                         for tag in new_tags]
            # Return the dict with the info
            return {'success': True, 'new': new_nodes, 'old': old_nodes}
        else:
            return {'success': False}

    # These are TAGS bipartite 1
    def get_child1(self, node, graph, state):
        tag = graph.nodes[node]['label']
        success, data = self.execute_artist_query(tag)

        if success:
            # Distinguish nodes previously seen from new nodes
            old_artists = [artist for artist in data if state.is_visited(0, artist)]
            new_artists = [artist for artist in data if not (state.is_visited(0, artist))]
            old_nodes = [state.visited_node(0, artist) for artist in old_artists]

            new_depth = graph.node[node]['_depth'] + 1
            new_nodes = [self.make_node_artist(artist, new_depth)
                         for artist in new_artists]
            return {'success': True, 'new': new_nodes, 'old': old_nodes}
        else:
            return {'success': False}

